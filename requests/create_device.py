from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException
import re

class CreateDeviceRequest(BaseModel):
	ip_address: str = Field(description='IP Address in IPV4 format XXX.XXX.XX.XX')
	description: str

	@field_validator('ip_address')
	def validate_ip_address(cls, value):
		ip_regex = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
		if not ip_regex.match(value):
			raise HTTPException(422, 'IP address has invalid format')
		
		return value