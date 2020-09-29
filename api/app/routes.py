from flask import Blueprint, request, jsonify
from app import __version__ as _api_version
import model_lstm
from model_lstm import __version__ as _model_lstm_version
from model_lstm.predict import predict_one, predict_many
from logging import getLogger

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
        return _api_version

@model_lstm_api.route('/v1/model_lstm/version', methods=['GET'])
def model_lstm_version():
    if request.method == 'GET':
        return _model_lstm_version

@model_lstm_api.route('/v1/model_lstm/test', methods=['GET'])
def model_lstm_test():
    if request.method == 'GET':
        logger.info("Test end point hit.")
        text = "This is great"
        pred = predict_one(text)
        response = {"text": text, "pred": int(pred)} # remove int() once model_lstm>=1.0.1
        return jsonify(response)