from sklearn.base import BaseEstimator, TransformerMixin
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

class TextEncoding(BaseEstimator, TransformerMixin):
    def __init__(self, num_words):
        self.tokenizer = Tokenizer(num_words=num_words, oov_token="OOV")

    def fit(self, X, y = None):
        self.tokenizer.fit_on_texts(X["text"])
        return self

    def transform(self, X):
        X = X.copy()
        X_encoded = self.tokenizer.texts_to_sequences(X["text"])
        return X_encoded

class SequencePadding(BaseEstimator, TransformerMixin):
    def __init__(self, max_length):
        self.max_length = max_length

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        X = X.copy()
        X_padded = pad_sequences(X, maxlen=self.max_length)
        return X_padded