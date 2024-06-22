from fastapi import APIRouter, Request
from requests import AuthorizeUserRequest
from middlewares import AuthMiddleware
from repositories import UserRepository
from repositories import AuthRepository

router = APIRouter()

@router.post('/')
def login(credentials: AuthorizeUserRequest, request: Request):
	if 'Authorization' in request.headers:
		return {'message': 'You are already logged in'}

	user_repository = UserRepository()
	is_valid_credentials = user_repository.is_valid_credentials(credentials=credentials)

	if not is_valid_credentials['success']:
		return {'message': is_valid_credentials['message']}
	
	user_uuid = user_repository.get_uuid_by_login(login=credentials.login)
	auth_repository = AuthRepository()
	return auth_repository.create_token_by_user_uuid(user_uuid=user_uuid)