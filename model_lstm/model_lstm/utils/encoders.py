from sklearn.base import BaseEstimator, TransformerMixin
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

class TextEncoding(BaseEstimator, TransformerMixin):
    def __init__(self, glove_embedding_path, embedding_matrix_path, num_words, embedding_dim, words_kept):
        self.tokenizer = Tokenizer(num_words=num_words, oov_token="OOV")
        self.glove_embedding_path = glove_embedding_path
        self.embedding_matrix_path = embedding_matrix_path
        self.num_words = num_words
        self.embedding_dim = embedding_dim
        self.words_kept = words_kept

    def fit(self, X, y = None):
        self.tokenizer.fit_on_texts(X["text"])
        self.build_embedding_matrix()
        return self

    def transform(self, X):
        X = X.copy()
        X_encoded = self.tokenizer.texts_to_sequences(X["text"])
        return X_encoded
    
    def build_embedding_matrix(self):
        embedding_dict = {}
        with open(self.glove_embedding_path) as f:
            for line in f:
                items = line.split()
                word = items[0]
                embedding = np.array(items[1:], dtype="float32")
                embedding_dict[word] = embedding
        
        num_tokens = len(self.tokenizer.word_index) + 2
        hits = 0
        misses = 0

        embedding_matrix = np.zeros((num_tokens, self.embedding_dim))
        for word, i in self.tokenizer.word_index.items():
            embedding_vector = embedding_dict.get(word)
            if embedding_vector is not None:
                embedding_matrix[i] = embedding_vector
                if i < (self.words_kept+2):
                    hits += 1
            else:
                if i < (self.words_kept+2):
                    misses += 1
        print(f"Converted {hits} words ({misses} misses) in words kept")
        np.save(self.embedding_matrix_path, embedding_matrix)


class SequencePadding(BaseEstimator, TransformerMixin):
    def __init__(self, max_length):
        self.max_length = max_length

    def fit(self, X, y = None):
        return self

    def transform(self, X):
        X = X.copy()
        X_padded = pad_sequences(X, maxlen=self.max_length)
        return X_padded

