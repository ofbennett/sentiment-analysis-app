from flask import Blueprint, request

basic_api = Blueprint("basic_api", __name__)
model_lstm_api = Blueprint("model_lstm_api", __name__)

@basic_api.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'