from flask import Blueprint, request, jsonify
from app import __version__ as _api_version
import model_lstm
from model_lstm import __version__ as _model_lstm_version
from model_lstm.predict import predict_one, predict_many
from logging import getLogger
from app.validation import validate_input_data

# Here __name__=="app". Careful not to conflict with name of 
# application.logger which is "sa_api" in this case
logger = getLogger(__name__)

basic_api = Blueprint("basic_api", __name__)
model_lstm_api = Blueprint("model_lstm_api", __name__)

@basic_api.route('/v1/health', methods=['GET'])
def health():
    logger.info("/v1/health endpoint hit.")
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

@model_lstm_api.route('/v1/model_lstm/predict_one', methods=['POST'])
def model_lstm_predict_one():
    if request.method == 'POST':
        valid, error_response = validate_request(request)
        if valid:
            json_data = request.get_json()
            text = json_data['text']
            pred_type = json_data['pred_type']
            if pred_type == 'hard':
                pred = predict_one(text)
            elif pred_type == 'soft':
                pred = predict_one(text, proba=True)
            response = {'pred': pred, 'model_lstm_version': _model_lstm_version, 'api_version': _api_version}
            return jsonify(response)
        else:
            return jsonify(error_response), 400

def validate_request(request):
    json_data = request.get_json()
    if json_data is None:
        logger.info('No JSON data in POST request')
        response = {'errors': 'No JSON data in POST request'}
        return False, response
    if json_data.get('text') is None:
        logger.info('No text field in JSON data of POST request')
        response = {'errors': 'No text field in JSON data of POST request'}
        return False, response
    if json_data.get('pred_type') is None:
        logger.info('No pred_type field in JSON data of POST request')
        response = {'errors': 'No pred_type field in JSON data of POST request'}
        return False, response
    errors = validate_input_data(json_data)
    if errors is not None:
        error_string = " ".join(errors['text'])
        logger.info(f'Invalid input: {error_string}')
        response = {'errors': errors}
        return False, response
    else:
        return True, None