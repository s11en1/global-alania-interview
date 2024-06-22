from models import AuthModel
from context_manager import get_session
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, timedelta
from dotenv import load_dotenv
import jwt
import os

load_dotenv()

class AuthRepository():
	def create_token_by_user_uuid(self, user_uuid: UUID):
		with get_session() as session:
			auth_model = AuthModel()
			auth_model.user_uuid = user_uuid
			auth_model.access_token = jwt.encode(
				payload={
					'sub': str(user_uuid)
				},
				algorithm='HS256',
				key=os.getenv('JWT_SECRET')
			)
			auth_model.expires = datetime.utcnow() + timedelta(hours=3)

			session.commit()

			return {
				'status': 'ok',
				'access_token': f'Bearer {auth_model.access_token}'
			}