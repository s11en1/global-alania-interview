from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from . import BaseModel
import uuid

class DeviceModel(BaseModel):
	__tablename__ = 'devices'

	id = Column(Integer, primary_key=True, autoincrement=True)
	uuid = Column(UUID(as_uuid=True),default=uuid.uuid4, unique=True, nullable=False)
	ip_address = Column(String, nullable=False)
	description = Column(String, nullable=False)