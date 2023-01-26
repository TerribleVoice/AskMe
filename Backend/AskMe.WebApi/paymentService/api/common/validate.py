import re
from typing import Optional
from uuid import UUID
from cerberus import Validator
from flask import Response
from db.models import Users, Tokens
from sqlalchemy.orm import Session


def validate_user_id(session: Session, user_id: UUID) -> Optional[Response]:
    q = session.query(Users).where(Users.id == user_id)
    user = session.execute(q).scalar()
    if not user:
        return Response(status=400, response=f"User with id {user_id} isn't found")
    elif not user.is_author:
        return Response(status=400, response=f"User is not author")
    return None


class CustomValidator(Validator):
    def _validate_is_uuid(self, is_uuid, field, value):
        """{'type': 'boolean' }"""
        re_uuid = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', re.I)
        if is_uuid and not re_uuid.match(value):
            self._error(field, 'invalid input syntax for type uuid')
