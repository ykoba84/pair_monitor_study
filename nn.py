#!/home/ykoba/anaconda3/envs/tenv/bin python
from keras.models import Model, Sequential
from keras.layers import Activation, Dense, Dropout, Input
from keras.layers import Conv2D, SeparableConv2D, MaxPooling2D
from keras.layers import Conv1D, MaxPooling1D, Flatten, GlobalAveragePooling1D
from keras.utils import plot_model
from keras.utils.np_utils import to_categorical
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adagrad
from keras.optimizers import Adam
from keras.optimizers import RMSprop

import matplotlib.pyplot as plt
import numpy as np
import time
import os
from datetime import datetime

# original pylib
import dataset as ds
import graph_plot as gpt
import outputs as otp

start = time.time()
date = datetime.now().strftime("%y%m%d_%H%M%S")

batch_size = 50
num_classes = 19
epochs = 10

# make train_data
x_train, y_train = ds.read_data_sigmay("../ML_Hans-on_Tutorial/train_data_sigmay_y0238")
# make test_data
x_test, y_test = ds.read_data_sigmay("../ML_Hans-on_Tutorial/test_data_sigmay_y0238")

# from list to array
x_train = np.array(x_train)
x_test = np.array(x_test)

# to predict
y_label = np.array(y_test)

# change list to categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Input layer as follows:
inputs = Input(shape=(64*64,))

# Hidden1 layer as follows:
h1 = Dense(100)(inputs)
#h1 = BatchNormalization()(h1)
h1 = Activation('relu')(h1)
#h1 = Dropout(0.5)(h1)
"""
# Hiddin2 layer as follows:
h2 = Dense(500)(h1)
#h2 = BatchNormalization()(h2)
h2 = Activation('relu')(h2)
#h2 = Dropout(0.5)(h2)

# Hiddin3 layer as follows:
h3 = Dense(500)(h2)
#h3 = BatchNormalization()(h3)
h3 = Activation('relu')(h3)
#h3 = Dropout(0.5)(h3)
"""
# Output layer as follows:
outputs = Dense(num_classes, activation='softmax')(h1)

model = Model(inputs=inputs, outputs=outputs)

model.summary()

model.compile(loss='categorical_crossentropy',
	      optimizer=Adam(lr=0.001),
              metrics=['accuracy'])

# return value each epochs
hist = model.fit(x_train, y_train,
                 batch_size=batch_size,
                 epochs=epochs,verbose=1,
                 validation_split=0.2)

# evaluate model
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

predictions = model.predict(x_test)
combinations = np.c_[y_label, predictions]

total_time = time.time() - start
print('Total time:', format(total_time) + '[sec]')

# outputs
outputpath = 'result/nn/' + date
os.makedirs(outputpath)
otp.ModelOutput(model, outputpath)
otp.EvaluateOutput(score, outputpath)
otp.CsvOutput_0238(combinations, outputpath)
otp.TotalTimeOutput(total_time, outputpath)
otp.HyperParameterOutput(batch_size, outputpath)
gpt.loss_and_acc(hist, epochs, outputpath)

sleeping_time = input("How long do you sleep?(hour) : ")
sleeping_time = int(sleeping_time)
if sleeping_time > 5:
    print("😃 < good!")
else:
    print("🤒 < bad...")
