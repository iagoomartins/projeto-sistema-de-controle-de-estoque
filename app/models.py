# models do banco de dados
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login

# tabela de usuário
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    # métodos da classe User
    # método para hashear a senha
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # método para verificar se a senha que foi fornecida corresponde ao hash armazenado
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# função do flask-login que carrega um usuário com base no ID da sessão.
# a função recebe o id e busca o usuario no banco de dados
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
# tabela de produto
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)