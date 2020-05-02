from app import app
from gevent.pywsgi import WSGIserver

if __name__ == "__main__":
    http_server = WSGIServer(('',5000),app)
    http_server.server_forever()
