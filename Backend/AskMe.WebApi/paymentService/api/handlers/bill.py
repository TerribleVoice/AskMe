from uuid import UUID
from flask import Response, current_app, request
from db.models import Users, Tokens
from sqlalchemy.orm import Session
from api.common.validate import CustomValidator, validate_user_id
from core.qiwiService.qiwiConnector import QiwiConnection

query_schema = {
    'receiver': {
        'type': 'string',
        'is_uuid': True,
        'required': True,
        'nullable': False,
    },
    'amount': {
        'type': 'float',
        'required': True,
        'nullable': False,
    },
    'sender': {
        'type': 'string',
        'required': False,
        'nullable': True
    },
    'comment': {
        'type': 'string',
        'required': False,
        'nullable': True
    }
}


def _get_token(session: Session, user_id: UUID) -> str:
    q = session.query(Tokens).where(Tokens.author_id == user_id)
    token_obj = session.execute(q).scalar()
    if not token_obj:
        raise Exception(f"User {user_id} hasn't token")
    return token_obj.token


def create_bill() -> Response:
    session: Session
    session_factory = current_app.session_factory
    validator_query = CustomValidator(query_schema)
    data = dict(request.json)
    if not validator_query.validate(data):
        return Response(status=400, response='Data validation error: %r.' % validator_query.errors)
    receiver_id, amount = data['receiver'], data['amount']
    with session_factory() as session:
        if res := validate_user_id(session, receiver_id):
            return res
        try:
            token = _get_token(session, receiver_id)
            qiwi_conn = QiwiConnection(token)
            pay_url, bill_id, _ = qiwi_conn.create_bill(amount)
            bill_updater = current_app.bill_updater
            bill_updater.put_bill(bill_id=bill_id, token=token, **data)
            return Response(status=200, response=pay_url)
        except Exception as ex:
            return Response(status=400, response=str(ex))
