from fastapi import APIRouter, Request
from middlewares import AuthMiddleware
from repositories import DeviceRepository
from requests import CreateDeviceRequest

router = APIRouter()

@router.get('/')
def get_devices_list(request: Request):
	AuthMiddleware.check_access_token(request)

	device_repository = DeviceRepository()
	return device_repository.get_list()

@router.post('/create')
def create_device(request: Request, device_data: CreateDeviceRequest):
	AuthMiddleware.check_access_token(request)
	
	device_repository = DeviceRepository()
	return device_repository.create(device_data=device_data)

@router.get('/{device_id}/terminals')
def get_terminals_list(request: Request, device_id: int):
	AuthMiddleware.check_access_token(request)

	device_repository = DeviceRepository()
	return device_repository.get_terminals_by_id(device_id)