import logging

from api.server import get_app
from billUpdater import BillUpdater

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils import make_pg_url
from config import config as cfg


def init_app():
    res = get_app()
    return res


if __name__ == '__main__':
    app = init_app()
    app.logger = logger = logging.getLogger(__name__)
    logger.info(f"Payment Service on port: {cfg.PORT=}")
    logger.info("Running...")
    engine = create_engine(make_pg_url(**cfg.DB_CONFIG))
    session_factory = sessionmaker(bind=engine)
    bill_updater = BillUpdater(1000, session_factory, logger)
    bill_updater.start()
    app.bill_updater = bill_updater
    app.session_factory = session_factory
    app.run(host="0.0.0.0", port=cfg.PORT, debug=True)

    bill_updater.stop()
    bill_updater.join()
