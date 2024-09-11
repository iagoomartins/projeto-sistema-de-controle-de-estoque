# ROTA DE PRODUTOS (ver produtos e adicionar produtos)
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import db
from app.models import Product

# instancia um objeto Blueprint = cria um blueprint de produtos
bp = Blueprint('product', __name__)

# rota para exibir todos os produtos
@bp.route('/products', methods=['GET', 'POST'])
@login_required
def index():
    products = Product.query.all()
    return render_template('products.html', products=products)


# rota para adicionar produtos
@bp.route('/product/add', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = float(request.form.get('description'))
        quantity = int(request.form.get('price'))
        product = Product(name=name, price=price, quantity=quantity)
        db.session.add(product)
        db.session.commit()
        flash('Produto adicionado com sucesso!')
        redirect(url_for('product.index'))
    return render_template('add_product.html')

