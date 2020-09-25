from sklearn.base import BaseEstimator, TransformerMixin
import re
from nltk.stem import SnowballStemmer
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

class TextCleaning(BaseEstimator, TransformerMixin):
    def __init__(self, regex):
        self.regex = regex

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        X = X.copy()
        X["text"] = X["text"].apply(lambda x: re.sub(self.regex, " ", x).strip())
        return X

class TextStemming(BaseEstimator, TransformerMixin):
    def __init__(self, skip=False):
        self.skip = skip

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        def _stem(x):
            stemmer = SnowballStemmer('english')
            final_tokens = []
            for token in x.split():
                token = stemmer.stem(token)
                final_tokens.append(token)
            x_stemmed = " ".join(final_tokens)
            return x_stemmed

        if self.skip:
            return X
        else:
            X = X.copy()
            X["text"] = X["text"].apply(_stem)
            return X

class TextStopWordRemoval(BaseEstimator, TransformerMixin):
    def __init__(self, skip=False, stop_words=[]):
        self.skip = skip
        self.stop_words = stop_words

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        def _removeStopWords(x):
            final_tokens = []
            for token in x.split():
                if token.lower() in self.stop_words:
                    continue
                final_tokens.append(token)
            x_sw_removed = " ".join(final_tokens)
            return x_sw_removed

        if self.skip:
            return X
        else:
            X = X.copy()
            X["text"] = X["text"].apply(_removeStopWords)
            return X


def convert_labels(label):
    convert_dict = {4: 1, 0: 0}
    new_label = convert_dict[label]
    return new_label