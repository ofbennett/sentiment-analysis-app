from tensorflow.keras import layers, Model, Input, initializers, Sequential
from tensorflow.keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasClassifier
import numpy as np
from model_lstm.config import config

def set_seeds():
    # Ensures model training is reproducible.
    seed_value = config.SEED
    import os
    os.environ['PYTHONHASHSEED']=str(seed_value)
    import random
    random.seed(seed_value)
    np.random.seed(seed_value)
    import tensorflow as tf
    tf.random.set_seed(seed_value)

def make_model():
    set_seeds()
    embedding_matrix = np.load(config.DATA_DIR / config.EMBEDDING_MATRIX_FILE)
    matrix_shape = embedding_matrix.shape
    embedding_layer = layers.Embedding(matrix_shape[0],
                                        matrix_shape[1],
                                        embeddings_initializer=initializers.Constant(embedding_matrix),
                                        trainable=False)

    model = Sequential()
    model.add(Input(shape=(config.PADDING_MAX_LENGTH,), dtype="int64"))
    model.add(embedding_layer)
    model.add(layers.Bidirectional(layers.LSTM(64)))
    model.add(layers.Dense(1, activation="sigmoid"))
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

def wrap_model():
    wrapped_model = KerasClassifier(build_fn=make_model, 
                                    batch_size=config.BATCH_SIZE, 
                                    validation_split=config.VALIDATION_PROP, 
                                    epochs=config.EPOCHS, 
                                    verbose=1)
    return wrapped_model

