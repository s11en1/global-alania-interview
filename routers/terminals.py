from fastapi import APIRouter, Request
from requests import CreateTerminalRequest
from repositories import TerminalRepository
from middlewares import AuthMiddleware

router = APIRouter()

@router.post('/create')
def create_terminal(request: Request, terminal_data: CreateTerminalRequest):
	AuthMiddleware.check_access_token(request)

	terminal_repository = TerminalRepository()
	return terminal_repository.create(terminal_data=terminal_data)

@router.delete('/delete/{terminal_id}')
def delete_terminal(request: Request, terminal_id: int):
	AuthMiddleware.check_access_token(request)

	terminal_repository = TerminalRepository()
	return terminal_repository.delete(terminal_id=terminal_id)