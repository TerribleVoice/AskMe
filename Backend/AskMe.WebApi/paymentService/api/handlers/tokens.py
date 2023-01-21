from flask import Response, current_app, request
from db.models import Users, Tokens
from sqlalchemy.orm import Session
from api.common.validate import CustomValidator, validate_user_id

query_schema = {
    'user_id': {
        'type': 'string',
        'is_uuid': True,
        'required': True,
        'nullable': False,
    },
    'token': {
        'type': 'string',
        'required': True,
        'nullable': False,
    },
}


def add_token() -> Response:
    session: Session
    session_factory = current_app.session_factory
    validator_query = CustomValidator(query_schema)
    data = dict(request.json)
    if not validator_query.validate(data):
        return Response(status=400, response='Data validation error: %r.' % validator_query.errors)
    user_id, token = data['user_id'], data['token']
    with session_factory() as session:
        if res := validate_user_id(session, user_id):
            return res
        q = session.query(Tokens).where(Tokens.author_id == user_id)
        token_obj = session.execute(q).scalar()
        if token_obj:
            session.query(Tokens).filter(Tokens.author_id == user_id).update(values={'token': token})
        else:
            session.add(Tokens(author_id=user_id, token=token))
        session.commit()
    return Response(status=200, response='Token was update for user: %s' % user_id)
