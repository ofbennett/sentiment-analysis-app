from flask import Flask

def create_app(config_object):
    flask_app = Flask("sa_api")
    flask_app.config.from_object(config_object)
    from app.routes import basic_api, model_lstm_api
    flask_app.register_blueprint(basic_api)
    flask_app.register_blueprint(model_lstm_api)
    return flask_app