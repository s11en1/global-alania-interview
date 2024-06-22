from fastapi import APIRouter, Request
from repositories import UserRepository
from requests import CreateUserRequest
from requests import UpdateUserRequest
from middlewares import AuthMiddleware

router = APIRouter()

@router.get('/')
def get_users_list(request: Request):
	AuthMiddleware.check_access_token(request)
	user_repository = UserRepository()
	return user_repository.get_list()

@router.post('/create')
def create_user(user_data: CreateUserRequest, request: Request):
	# AuthMiddleware.check_access_token(request)
	user_repository = UserRepository()
	return user_repository.create(user_data=user_data)

@router.delete('/delete/{user_id}')
def delete_user(user_id: int, request: Request):
	AuthMiddleware.check_access_token(request)
	user_repository = UserRepository()
	return user_repository.delete(user_id)

@router.patch('/update')
def update_user(user_data: UpdateUserRequest, request: Request):
	user = AuthMiddleware.check_access_token(request)
	user_repository = UserRepository()
	return user_repository.update(user_data=user_data, user_uuid=user['user_uuid'])