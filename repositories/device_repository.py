from context_manager import get_session
from models import DeviceModel, TerminalModel
from fastapi import HTTPException
from requests import CreateDeviceRequest

class DeviceRepository:
	def get_list(self):
		with get_session() as session:
			result = []
			devices = session.query(DeviceModel).all()
			for device in devices:
				result.append({
					'id': device.id,
					'ip': device.ip_address
				})
		
		return result
	
	def create(self, device_data: CreateDeviceRequest):
		ip_address = device_data.ip_address
		description = device_data.description

		with get_session() as session:
			device = DeviceModel()

			device.ip_address = ip_address
			device.description = description

			session.add(device)

		return {'status': 'ok'}
	
	def get_terminals_by_id(self, device_id: int):
		with get_session() as session:
			if session.query(DeviceModel).filter_by(id=device_id).count() == 0:
				raise HTTPException(404, 'Device with this id was not found')
			
			device_uuid = session.query(DeviceModel).filter_by(id=device_id).first().uuid
			result =  []

			terminals = session.query(TerminalModel).filter_by(device_uuid=device_uuid).all()

			for terminal in terminals:
				result.append({
					'id': terminal.id,
					'mac': terminal.mac,
					'model': terminal.model
				})

		return result