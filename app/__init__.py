from flask import Flask
from flask import request
from .blueprints.user_blueprint import user_blueprint
from .blueprints.name_blueprint import name_blueprint
import os
import pdb
from flask import jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import click

def create_app(test_config=None, env=None):
    root_path = os.path.abspath('.')
    config_path = os.path.join(root_path, 'config')
    app = Flask('__name__', instance_relative_config=True, instance_path=config_path, template_folder='app/templates')

    app.config['JSON_AS_ASCII'] = False

    if env:
        app.config['ENV'] = env

    if test_config:
        app.config.from_mapping(test_config)

    app.config.from_object("config.{}".format(app.config['ENV'].capitalize()))

    app.register_blueprint(user_blueprint)
    app.register_blueprint(name_blueprint)


    engine = create_engine(app.config['DB_URL'])
    app.dbsession = sessionmaker(bind=engine)

    @app.route('/', methods=['GET'])
    def root():
        response_body = dict(message="Welcome!")
        return jsonify(response_body)


    @app.cli.command("console")
    def run_console():
        os.system('PYTHONPATH=. python3 -i ./test/test_load_all.py')

    @app.cli.command("test")
    @click.argument("path")
    def test_file(path):
        os.system('PYTHONPATH=. python3 {}'.format(path))


    return app

if __name__ == "__main__":
    app = create_app()
    app.run()