from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from . import BaseModel
import uuid

class AuthModel(BaseModel):
	__tablename__ = 'auth'

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
	user_uuid = Column(ForeignKey('users.uuid', ondelete='CASCADE'), unique=True, nullable=False)
	access_token = Column(String, nullable=False)
	expires = Column(DateTime, nullable=False)