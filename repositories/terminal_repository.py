from requests import CreateTerminalRequest
from context_manager import get_session
from models import DeviceModel, TerminalModel
from fastapi import HTTPException

class TerminalRepository():
	def create(self, terminal_data: CreateTerminalRequest):
		device_id = terminal_data.device_id
		mac_address = terminal_data.mac_address
		model = terminal_data.model

		with get_session() as session:
			if(session.query(DeviceModel).filter_by(id=device_id).count() == 0):
				raise HTTPException(404, 'Device with this id was not found')
			
			device_uuid = session.query(DeviceModel).filter_by(id=device_id).first().uuid

			terminal = TerminalModel()

			terminal.device_uuid = device_uuid
			terminal.mac = mac_address
			terminal.model = model

			session.add(terminal)

			return {'status': 'ok'}

	def delete(self, terminal_id: int):
		with get_session() as session:
			if session.query(TerminalModel).filter_by(id=terminal_id).count() == 0:
				raise HTTPException(404, 'Terminal with this id was not found')
			
			session.query(TerminalModel).filter_by(id=terminal_id).delete()
		
		return {'status': 'ok'}