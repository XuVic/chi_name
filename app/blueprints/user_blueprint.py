from flask import Blueprint
from flask import abort
from flask import render_template
from flask import current_app
from flask import g
from flask import session
import pdb


user_blueprint = Blueprint('user', __name__, url_prefix='/user')

@user_blueprint.route('/index', methods=['GET', 'POST'])
def index():
    session['test'] = 123
    g.setdefault('test', 'this is global')
    print(g.pop('test'))
    return render_template('index.html')

@user_blueprint.route('/test')
def test2():
    return '123'

@user_blueprint.errorhandler(404)
def error(e):
    return 'error in user blueprint'