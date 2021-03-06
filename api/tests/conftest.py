import pytest

from app.app import create_app
from app.config import TestingConfig

@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app

@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client

@pytest.fixture
def easy_sentiment_examples():
    test_examples = ["This is great", 
                     "This is terrible", 
                     "I'm so happy",
                     "I feel awful.",
                     "I have wonderful news!"]
    target_examples = [1, 0, 1, 0, 1] # 1=positive, 0=negative
    
    return test_examples, target_examples

@pytest.fixture
def validation_examples():
    test_examples = ["This is great", 
                     "", 
                     "a"*1500,
                     "feowgaoeinbao",
                     "I have wonderful news!",
                     None,
                     "1234",
                     1234]
    target_status_codes = [200, 400, 400, 200, 200, 400, 200, 400]
    return test_examples, target_status_codes