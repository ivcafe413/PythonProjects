# Regression example
import tensorflow as tf
from tensorflow import keras

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

print(tf.__version__)

# Housing price prediction
housing = keras.datasets.boston_housing
(train_data, train_labels), (test_data, test_labels) = housing.load_data()

# Shuffle the data
order = np.argsort(np.random.random(train_labels.shape))
train_data = train_data[order]
train_labels = train_labels[order]

# Normalization. Test data not in use for calcs of mean & std
mean = train_data.mean(axis=0)
std = train_data.std(axis=0)
train_data = (train_data - mean) / std
test_data = (test_data - mean) / std

# Defs
def build_model():
    model = keras.Sequential([
        keras.layers.Dense(64, activation=tf.nn.relu,
        input_shape=(train_data.shape[1],)),
        keras.layers.Dense(64, activation=tf.nn.relu),
        keras.layers.Dense(1)
    ])

    optimizer = tf.train.RMSPropOptimizer(0.001)

    model.compile(loss='mse',
        optimizer=optimizer,
        metrics=['mae'])
    return model

class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self,epoch,logs):
        if epoch % 100 == 0: print('')
        print('.', end='')

model = build_model()
model.summary()

EPOCHS = 500

# Store training stats
early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)

history = model.fit(train_data, train_labels, epochs=EPOCHS,
                    validation_split=0.2, verbose=0,
                    callbacks=[early_stop, PrintDot()])

def plot_history(history):
  pyplot.figure()
  pyplot.xlabel('Epoch')
  pyplot.ylabel('Mean Abs Error [1000$]')
  pyplot.plot(history.epoch, np.array(history.history['mean_absolute_error']), 
           label='Train Loss')
  pyplot.plot(history.epoch, np.array(history.history['val_mean_absolute_error']),
           label = 'Val loss')
  pyplot.legend()
  pyplot.ylim([0,5])
  pyplot.show()

plot_history(history)

[loss, mae] = model.evaluate(test_data, test_labels, verbose=0)

print("Testing set Mean Abs Error: ${:7.2f}".format(mae * 1000))

test_predictions = model.predict(test_data).flatten()

print(test_predictions)