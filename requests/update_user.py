from pydantic import BaseModel

class UpdateUserRequest(BaseModel):
	fullname: str