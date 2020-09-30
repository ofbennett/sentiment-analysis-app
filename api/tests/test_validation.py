def test_input_data_validation(flask_test_client, validation_examples):
    test_examples, target_status_codes = validation_examples
    for i, text in enumerate(test_examples):
        post_json_data = {'text': text}
        response = flask_test_client.post('/v1/model_lstm/predict_one', json=post_json_data)
        assert response.status_code == target_status_codes[i]