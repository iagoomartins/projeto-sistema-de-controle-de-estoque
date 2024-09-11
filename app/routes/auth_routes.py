# ROTA DE AUTENTICAÇÃO (LOGIN E LOGOUT)
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import db
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request
from app.forms import RegistrationForm

# instancia um objeto Blueprint = cria um blueprint de autenticação
bp = Blueprint('auth', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("product.index"))
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            flash('Usuário ou senha incorretos!')
            return redirect(url_for("auth.login"))
        login_user(user)
        return redirect(url_for('product.index'))
    return render_template('login.html')


# rota de cadastro de usuário
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('product.index'))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        # Cria o novo usuário
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        
        # Salva o usuário no banco de dados
        db.session.add(user)
        db.session.commit()
        
        flash('Parabéns, registro concluido com sucesso!')
        login_user(user)
        return redirect(url_for('product.index'))
    
    return render_template('register.html', title='Register', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))