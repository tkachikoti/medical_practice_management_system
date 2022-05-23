import os

from flask import Flask

from flask import redirect
from flask import url_for


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register database functions with the Flask app.
    from . import db
    db.init_app(app)

    # apply the blueprints to the app
    from . import services

    app.register_blueprint(services.bp)

    # a simple page that says hello
    @app.route('/')
    def index():
        return redirect(url_for('services.index'))

    return app