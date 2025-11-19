from flask import render_template
from . import main
from flask_login import login_required, current_user

@main.route('/')
@login_required
def index():
    from app.models import User
    usuarios = User.query.all()
    return render_template('index.html', usuarios=usuarios)
