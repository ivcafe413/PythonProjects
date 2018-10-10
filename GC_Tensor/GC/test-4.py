import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as pyplot

print(tf.__version__)

NUM_WORDS = 10000

(train_data, train_labels), (test_data, test_labels) = keras.datasets.imdb.load_data(num_words=NUM_WORDS)

# Multi-hot encoding func
def multi_hot_encode(sequences, dimensions):
    # All-zero matrix of shape (len(sequences), dimensions)
    results = np.zeros((len(sequences), dimensions))
    for i, word_indices in enumerate(sequences):
        results[i, word_indices] = 1.0 # 1s
    return results

# Shuffle the training set
order = np.argsort(np.random.random(train_labels.shape)) # 
train_data = train_data[order]
train_labels = train_labels[order]

train_data = multi_hot_encode(train_data, NUM_WORDS)
test_data = multi_hot_encode(test_data, NUM_WORDS)

# Baseline
baseline = keras.Sequential([
    keras.layers.Dense(16, activation=tf.nn.relu, input_shape=(10000,)),
    keras.layers.Dense(16, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.sigmoid)
])
baseline.compile(optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', 'binary_crossentropy'])
baseline.summary()

baseline_history = baseline.fit(train_data, train_labels,
    epochs=20, batch_size=512,
    validation_data=(test_data, test_labels), verbose=2)

# Smaller
