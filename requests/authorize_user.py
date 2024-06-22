from pydantic import BaseModel

class AuthorizeUserRequest(BaseModel):
	login: str
	password: str