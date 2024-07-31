from wtforms_alchemy import ModelForm, Unique
from models.user import User
from wtforms import PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp
from utils.extensions import db

class RegistrationForm(ModelForm):
    class Meta:
        model = User
        only = ['username', 'email']  # Only include fields that match the model directly
        field_args = {
            'username': {
                'validators': [
                    DataRequired(),
                    Unique(User.username, get_session=lambda: db.session)
                ]
            },
            'email': {
                'validators': [
                    DataRequired(),
                    Unique(User.email, get_session=lambda: db.session)
                ]
            }
        }

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=4, message='Password must be at least 4 characters long.'),
        EqualTo('confirm', message='Passwords must match.'),
        Regexp(r'^[^\s]+$', message='Password must not contain any spaces.')
    ])
    confirm = PasswordField('Confirm Password')
