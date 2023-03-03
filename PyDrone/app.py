from flask import Flask
from tello import tello

app = Flask(__name__)

app.register_blueprint(tello, url_prefix='')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
