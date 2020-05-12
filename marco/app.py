import os
import logging
from flask import Flask
import nartan

#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)
app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(nartan.bp)
app.add_url_rule('/', endpoint='index')
app.run(host='0.0.0.0')
