# formulário de cadastro
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password',
        message='As senhas devem combinar.')])
    submit = SubmitField('Submit')
    
    # validação personalizada para garantir que o username seja unico
    def validate_username(self, username):
        user = User.query.filter_by(username=username).first()
        if user is not None:
            raise ValidationError('Este nome de usuário já está em uso.')
            