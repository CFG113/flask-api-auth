from utils.extensions import bcrypt
from werkzeug.exceptions import InternalServerError, Unauthorized
from repositories.user_repository import UserRepository
from models.user import User
from sqlalchemy.exc import SQLAlchemyError
from forms.registration_form import RegistrationForm
class UserService:
    @staticmethod
    def create_user(form: RegistrationForm) -> User:
        try:
            # Hash the password
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

            # Create a new user instance
            user = User(
                username=form.username.data,
                email=form.email.data,
                password_hash=hashed_password
            )

            # Save the user to the database
            created_user = UserRepository.create_user(user)
            return created_user
        except SQLAlchemyError as e:
            raise InternalServerError(f"Database error creating user '{form.username.data}': {str(e)}")

    @staticmethod
    def login_user(username: str, password: str) -> User:
        try:
            user = UserRepository.get_user_by_username(username)
            if not user:
                raise Unauthorized("Invalid username or password.")

            if not bcrypt.check_password_hash(user.password_hash, password):
                raise Unauthorized("Invalid username or password.")

            return user
        except SQLAlchemyError as e:
            raise InternalServerError(f"Database error retrieving user '{username}': {str(e)}")