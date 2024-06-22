from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from . import BaseModel
from datetime import datetime
import uuid

class TerminalModel(BaseModel):
	__tablename__ = 'terminals'

	id = Column(Integer, primary_key=True, autoincrement=True) 
	uuid = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False)
	device_uuid = Column(ForeignKey('devices.uuid', ondelete='CASCADE'), nullable=False)
	mac = Column(String, nullable=False)
	model = Column(String, nullable=False)
	dt_created = Column(DateTime, default=datetime.utcnow, nullable=False)
	dt_last_pool = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)