from model_lstm.utils.preprocessors import TextCleaning, TextStopWordRemoval
from model_lstm.config import config
import pandas as pd
import re

def test_textcleaning(text_cleaning_test_examples):
    cleaned_text = []
    for text in text_cleaning_test_examples:
        cleaned_text.append( re.sub(config.TEXT_CLEANING_REGEX, " ", text).strip() )

    text_cleaning_test_examples_df = pd.DataFrame({"text": text_cleaning_test_examples})
    textcleaner = TextCleaning(regex=config.TEXT_CLEANING_REGEX)
    textcleaner.fit(text_cleaning_test_examples_df)

    # Test that fit method does not modify text
    for i in range(len(text_cleaning_test_examples)):
        assert text_cleaning_test_examples_df["text"][i] == text_cleaning_test_examples[i]
    
    text_cleaning_test_examples_df = textcleaner.transform(text_cleaning_test_examples_df)

    # Test that transform method cleans text according to the chosen regex
    for i in range(len(text_cleaning_test_examples)):
        assert text_cleaning_test_examples_df["text"][i] == cleaned_text[i]

def test_stopWordRemoval(stop_word_removal_test_examples):
    stop_word_removal_test_examples_df = pd.DataFrame({"text": stop_word_removal_test_examples})

    stopWordRemover = TextStopWordRemoval(skip=False, stop_words=config.STOP_WORDS)
    stopWordRemover.fit(stop_word_removal_test_examples_df)

    # Test that fit method does not modify text
    for i in range(len(stop_word_removal_test_examples)):
        assert stop_word_removal_test_examples_df["text"][i] == stop_word_removal_test_examples[i]

    stop_word_removal_test_examples_df = stopWordRemover.transform(stop_word_removal_test_examples_df)

    # Test that stop words are all removed (case insensitive)
    for i in range(len(stop_word_removal_test_examples)):
        for word in config.STOP_WORDS:
            assert word.lower() not in stop_word_removal_test_examples_df["text"][i].lower().split()