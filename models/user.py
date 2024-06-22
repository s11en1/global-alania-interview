from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from . import BaseModel
import uuid

class UserModel(BaseModel):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
	login = Column(String, unique=True, nullable=False)
	password = Column(String(255), nullable=False)
	fullname = Column(String, nullable=False)
	status = Column(Integer, default=0)

	CheckConstraint('status >= 0 AND status <=3', name="check_status_range")