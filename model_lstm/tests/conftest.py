import pytest

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
def text_cleaning_test_examples():
    test_examples = ["This is great",
                     "I feel awful.",
                     "I have wonderful news!",
                     "My email is robert341235@aol.com",
                     "Sarah follows @google and @tom_smith. She told me yesterday.",
                     "",
                     "!%&$",
                     "elfioev@gmail.com"]
    return test_examples

@pytest.fixture
def stop_word_removal_test_examples():
    test_examples = ["I am going to this house.",
                     "If you hear this then that is fine $%&",
                     "the apple and the pear are both fruits. My email is fig3533@hotmal.com    "]
    return test_examples