from app import __version__ as _api_version
from model_lstm import __version__ as _model_lstm_version

def test_health_endpoint(flask_test_client):
    response = flask_test_client.get('/v1/health')
    assert response.status_code == 200

def test_api_version_endpoint(flask_test_client):
    response = flask_test_client.get('/v1/api_version')
    json_data = response.get_json()
    api_version = json_data['api_version']
    assert api_version == _api_version

def test_model_lstm_version_endpoint(flask_test_client):
    response = flask_test_client.get('/v1/model_lstm/version')
    json_data = response.get_json()
    model_lstm_version = json_data['model_lstm_version']
    assert model_lstm_version == _model_lstm_version

def test_predict_one_endpoint(flask_test_client, easy_sentiment_examples):
    test_examples, target_examples = easy_sentiment_examples
    for i, text in enumerate(test_examples):
        post_json_data = {'text': text, 'pred_type': 'hard'}
        response = flask_test_client.post('/v1/model_lstm/predict_one', json=post_json_data)
        assert response.status_code == 200
        response_json_data = response.get_json()
        pred = response_json_data['pred']
        api_version = response_json_data['api_version']
        model_lstm_version = response_json_data['model_lstm_version']
        assert pred == target_examples[i]
        assert api_version == _api_version
        assert model_lstm_version == _model_lstm_version

def test_predict_one_proba_endpoint(flask_test_client, easy_sentiment_examples):
    test_examples, target_examples = easy_sentiment_examples
    for i, text in enumerate(test_examples):
        post_json_data = {'text': text, 'pred_type': 'soft'}
        response = flask_test_client.post('/v1/model_lstm/predict_one', json=post_json_data)
        assert response.status_code == 200
        response_json_data = response.get_json()
        pred = response_json_data['pred']
        api_version = response_json_data['api_version']
        model_lstm_version = response_json_data['model_lstm_version']
        assert type(pred) is float
        assert pred > 0
        assert pred < 1
        pred = 1 if pred > 0.5 else 0
        assert pred == target_examples[i]
        assert api_version == _api_version
        assert model_lstm_version == _model_lstm_version