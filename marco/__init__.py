import os
from flask import Flask

#https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import nartan
    app.register_blueprint(nartan.bp)
    app.add_url_rule('/', endpoint='index')
    return app


