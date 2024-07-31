from typing import Optional
from models.user import User
from utils.extensions import db
from sqlalchemy.exc import SQLAlchemyError

class UserRepository:
    @staticmethod
    def create_user(user: User) -> User:
        try:
            db.session.add(user)
            db.session.commit()
            return user
        except SQLAlchemyError:
            db.session.rollback()
            raise

    @staticmethod
    def get_all_users() -> list[User]:
        try:
            return User.query.all()
        except SQLAlchemyError:
            raise

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        try:
            return User.query.get(user_id)
        except SQLAlchemyError:
            raise

    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        try:
            return User.query.filter_by(username=username).first()
        except SQLAlchemyError:
            raise

    @staticmethod
    def get_user_by_email(email: str) -> Optional[User]:
        try:
            return User.query.filter_by(email=email).first()
        except SQLAlchemyError:
            raise

    @staticmethod
    def update_user(user: User) -> User:
        try:
            db.session.merge(user)
            db.session.commit()
            return user
        except SQLAlchemyError:
            db.session.rollback()
            raise
    
    @staticmethod
    def delete_user(user: User) -> bool:
        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except SQLAlchemyError:
            db.session.rollback()
            raise
