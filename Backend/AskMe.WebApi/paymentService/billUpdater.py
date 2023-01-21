from uuid import UUID
import logging
import time
from time import sleep
from queue import Empty, Full, Queue
from threading import Event, Thread
from typing import List, Optional, Dict

from core.qiwiService.qiwiConnector import QiwiConnection
from db.models import Bills

logger = logging.getLogger(__name__)


class BillUpdater(Thread):
    def __init__(self, queue_max_size: int, session_factory):
        super().__init__(name=self.__class__.__name__)
        self._stop_event = Event()
        self.interval = 2
        self._queue = Queue(maxsize=queue_max_size)
        self._last_message_time = 0

        self._session_factory = session_factory

    def run(self):
        logger.info(f"Starting {self.__class__.__name__}")

        while not self._stop_event.is_set():
            try:
                self._check()
            except Empty:
                pass
            except Exception as exp:
                logger.exception(f"Unexpected error: {exp}")
            sleep(300)
        logger.info(f"{self.__class__.__name__} stopped")

    def stop(self, timeout=None):
        logger.info(f"Stopping {self.__class__.__name__}")
        self._stop_event.set()

    def put_bill(self, bill_id: UUID, token: str, receiver: UUID, amount: float, sender: Optional[str] = None,
                 comment: Optional[str] = None, put_timeout: Optional[int] = None) -> None:
        message = {'bill_id': bill_id, 'token': token, 'receiver': receiver, 'sender': sender, 'comment': comment,
                   'amount': amount}
        try:
            self._queue.put(message, block=put_timeout is not None, timeout=put_timeout)
        except Full:
            # Логируем не чаще чем раз в 5 минут
            if (time.monotonic() - self._last_message_time) > 300:
                logger.warning(f'Bills queue full, bill with id {message["bill_id"]} is skipped')
                self._last_message_time = time.monotonic()

    def _check(self):
        logger.debug(f'Check bills, {self._queue.qsize()} bills count')
        for _ in range(100):
            data: Dict = self._queue.get(timeout=3)
            token, bill_id = data['token'], data['bill_id']
            try:
                qiwi_conn = QiwiConnection(token)
                status, _ = qiwi_conn.check_bill(bill_id)
                if status == 'WAITING':
                    self.put_bill(**data)
                elif status == 'PAID':
                    data.pop('token')
                    data.pop('amount')
                    with self._session_factory() as session:
                        session.add(Bills(**data))
                        session.commit()
                else:
                    qiwi_conn.remove_bill(bill_id)
            except Exception as ex:
                self.put_bill(**data)
                raise Exception(f'{ex}')
