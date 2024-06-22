from pydantic import BaseModel

class CreateUserRequest(BaseModel):
	login: str
	password: str
	fullname: str