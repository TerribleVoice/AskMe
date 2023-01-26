from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True)
    login = Column(String)
    email = Column(String)
    password = Column(String)
    is_author = Column(Boolean)


class Tokens(Base):
    __tablename__ = 'tokens'

    author_id = Column(UUID(as_uuid=True), ForeignKey(Users.id), nullable=False, primary_key=True)
    token = Column(String, nullable=False)
