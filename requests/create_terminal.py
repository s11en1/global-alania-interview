from pydantic import BaseModel, Field, field_validator
from fastapi import HTTPException
import re

class CreateTerminalRequest(BaseModel):
	device_id: int
	mac_address: str = Field(description='MAC address in format XX:XX:XX:XX:XX:XX')
	model: str

	@field_validator('mac_address')
	def validate_mac_address(cls, value):
		mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
		if not mac_regex.match(value):
			raise HTTPException(422, 'MAC address has invalid format')
		
		return value