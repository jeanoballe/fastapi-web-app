from typing import Optional
from webapp.data.user import User
from webapp.data import db_session


def user_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(User).count()
    finally:
        session.close()


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, 'abc')


def login_user(email: str, password: str) -> Optional[User]:
    if password == 'abc':
        return User("test user", email, 'abc')

    return None