import pytest

@pytest.fixture
def easy_sentiment_examples():
    test_examples = ["This is great", 
                     "This is terrible", 
                     "I'm so happy",
                     "I feel awful.",
                     "I have wonderful news!"]
    target_examples = [1, 0, 1, 0, 1]
    fixture = {"test": test_examples, "target": target_examples}
    return fixture