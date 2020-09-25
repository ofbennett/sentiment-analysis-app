from tensorflow.keras import layers, Model, Input, initializers
from tensorflow.keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasClassifier
import numpy as np
from model_lstm.config import config

def make_model():
    embedding_matrix = np.load(config.DATA_DIR / config.EMBEDDING_MATRIX_FILE)
    matrix_shape = embedding_matrix.shape
    embedding_layer = layers.Embedding(matrix_shape[0],
                                        matrix_shape[1],
                                        embeddings_initializer=initializers.Constant(embedding_matrix),
                                        trainable=False)

    int_sequences_input = Input(shape=(config.PADDING_MAX_LENGTH,), dtype="int64")
    embedded_sequences = embedding_layer(int_sequences_input)
    x = layers.Bidirectional(layers.LSTM(64, dropout=0.2, recurrent_dropout=0.2))(embedded_sequences)
    preds = layers.Dense(1, activation="sigmoid")(x)

    model = Model(int_sequences_input, preds)
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    
    return model

def wrap_model():
    wrapped_model = KerasClassifier(build_fn=make_model, 
                                    batch_size=config.BATCH_SIZE, 
                                    validation_split=config.VALIDATION_PROP, 
                                    epochs=config.EPOCHS, 
                                    verbose=1)
    return wrapped_model

