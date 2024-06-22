from models import UserModel
from context_manager import get_session
from requests import CreateUserRequest, AuthorizeUserRequest, UpdateUserRequest
import bcrypt

class UserRepository():
	def get_list(self):
		result = []

		with get_session() as session:
			users = session.query(UserModel).all()

			for user in users:
				result.append({
					'id': user.id,
					'login': user.login,
					'fullname': user.fullname
				})

		return result

	def create(self, user_data: CreateUserRequest):
		with get_session() as session:
			if(session.query(UserModel).filter_by(login=user_data.login).count() > 0):
				return {'message': 'User with this login already exist'}

			hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())

			user = UserModel()
			user.login = user_data.login
			user.password = hashed_password.decode('utf-8')	
			user.fullname = user_data.fullname

			session.add(user)
			session.commit()

			return {'id':user.id, 'uuid': user.uuid, 'fullname': user.fullname, 'login': user.login}
		
	def delete(self, user_id: int):
		with get_session() as session:
			if session.query(UserModel).filter_by(id=user_id).count() == 0:
				return {'message': 'This user doesn\'t exist'}
			
			session.query(UserModel).filter_by(id=user_id).delete()
			return {'messaage': 'User was deleted successfully'}
		
	def is_valid_credentials(self, credentials: AuthorizeUserRequest):
		with get_session() as session:
			login = credentials.login
			password = credentials.password

			if session.query(UserModel).filter_by(login=login).count() == 0:
				return { 
					'success': False,
					'message': 'User with this login doesn\'t exist'
				}
			
			user = session.query(UserModel).filter_by(login=login).first()
			if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
				return {
					'success': False,
					'message': 'Incorrect password'
				}
			
			return {'success': True}
		
	def get_uuid_by_login(self, login: str):
		with get_session() as session:
			user_uuid = session.query(UserModel).filter_by(login=login).first().uuid
			return user_uuid

	def is_valid_uuid(self, uuid: str):
		with get_session() as session:
			return session.query(UserModel).filter_by(uuid=uuid).count() > 0
		
	def update(self, user_data: UpdateUserRequest, user_uuid: str):
		with get_session() as session:
			user = session.query(UserModel).filter_by(uuid=user_uuid).first()
			user.fullname = user_data.fullname
			session.commit()

			return {'success': True, 'message': 'User was updated successfully'}
