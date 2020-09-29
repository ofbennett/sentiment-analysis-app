from flask import Flask

def create_app():
    flask_app = Flask("sa_api")
    from app.routes import basic_api, model_lstm_api
    flask_app.register_blueprint(basic_api)
    flask_app.register_blueprint(model_lstm_api)
    return flask_app