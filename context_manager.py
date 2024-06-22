from contextlib import contextmanager
from database import Session

@contextmanager
def get_session():
	session = Session()
	try:
		yield session
		session.commit()
	except:
		session.rollback()
		raise
	finally:
		session.close()