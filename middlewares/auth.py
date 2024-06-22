import jwt
import os
from dotenv import load_dotenv
from fastapi import HTTPException, Request

load_dotenv()

class AuthMiddleware():
	@staticmethod
	def check_access_token(request: Request):
		request_headers = request.headers

		if 'Authorization' not in request_headers:
			raise HTTPException(403, detail='Access forbidden')
		
		access_token = request_headers['Authorization']

		if 'Bearer ' not in access_token:
			raise HTTPException(403, detail='Access forbidden')
		
		clear_token = access_token.replace('Bearer ', '')

		try:
			payload = jwt.decode(jwt=clear_token, key=os.getenv('JWT_SECRET'), algorithms=['HS256', 'RS256'])
			from repositories import UserRepository
			user_repository = UserRepository()

			is_valid_uuid = user_repository.is_valid_uuid(uuid=payload['sub'])	
			if not is_valid_uuid:
				raise HTTPException(403, detail='Access forbidden')
			
			return {'success': True, 'user_uuid': payload['sub']}
		except jwt.InvalidTokenError:
			raise HTTPException(403, detail='Access forbidden')