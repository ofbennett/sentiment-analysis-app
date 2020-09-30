from flask import Blueprint, request, jsonify
from app import __version__ as _api_version
import model_lstm
from model_lstm import __version__ as _model_lstm_version
from model_lstm.predict import predict_one, predict_many
from logging import getLogger

# Here __name__=="app". Careful not to conflict with name of 
# application.logger which is "sa_api" in this case
logger = getLogger(__name__)

basic_api = Blueprint("basic_api", __name__)
model_lstm_api = Blueprint("model_lstm_api", __name__)

@basic_api.route('/v1/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'

@basic_api.route('/v1/api_version', methods=['GET'])
def api_version():
    if request.method == 'GET':
        response = {'api_version': _api_version}
        return jsonify(response)

@model_lstm_api.route('/v1/model_lstm/version', methods=['GET'])
def model_lstm_version():
    if request.method == 'GET':
        response = {'model_lstm_version': _model_lstm_version}
        return jsonify(response)

@model_lstm_api.route('/v1/model_lstm/test', methods=['GET'])
def model_lstm_test():
    if request.method == 'GET':
        logger.info("Test end point hit.")
        text = "This is great"
        pred = predict_one(text)
        pred = int(pred) # remove this line once model_lstm>=1.0.1
        response = {"text": text, "pred": pred} 
        return jsonify(response)

@model_lstm_api.route('/v1/model_lstm/predict_one', methods=['POST'])
def model_lstm_predict_one():
    if request.method == 'POST':
        json_data = request.get_json()
        text = json_data['text']
        pred = predict_one(text)
        pred = int(pred) # remove this line once model_lstm>=1.0.1
        response = {'pred': pred, 'model_lstm_version': _model_lstm_version, 'api_version': _api_version}
        return jsonify(response)