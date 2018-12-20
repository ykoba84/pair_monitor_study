from keras.models import Model, Sequential
from keras.layers import Activation, Dense, Dropout, Input
from keras.layers import Conv2D, SeparableConv2D, MaxPooling2D
from keras.layers import Conv1D, MaxPooling1D, Flatten, GlobalAveragePooling1D
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
print("time stamp :", date)

batch_size = 64
num_classes = 10
epochs = 300

print("hyper parameteres : batch_size=", batch_size, "epochs=", epochs)

# make train_data
x_train, y_train = ds.read_data("train_data_lowLumi")
#x_train, y_train = ds.read_60k("train_data_60k")
# make test_data
x_test, y_test = ds.read_data("test_data_5000")

# from list to array
x_train = np.array(x_train)
x_test = np.array(x_test)

#print(x_train.shape)

x_train = x_train.reshape(x_train.shape[0], 64, 64, 1)
x_test = x_test.reshape(x_test.shape[0], 64, 64, 1)

# to predict
y_label = np.array(y_test)

# change list to categorical
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#print(y_train.shape)

# set loss
imagedim = (64,64,1)
nFiltersPerStep = 4

# using functional API
inputs = Input( shape=imagedim )
# conv1
x = Conv2D(filters=nFiltersPerStep, kernel_size=3, strides=1, padding='same' )(inputs)
#x = Activation('relu')(x)
x = Conv2D(filters=nFiltersPerStep, kernel_size=3, strides=1, padding='same' )(x)
x = BatchNormalization()(x)
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
# Conv2
x = Conv2D(filters=nFiltersPerStep, kernel_size=3, strides=1, padding='same')(x)
#x = Activation('relu')(x)
x = Conv2D(filters=nFiltersPerStep, kernel_size=3, strides=1, padding='same')(x)
x = BatchNormalization()(x)
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
x = Dropout(0.33)(x)
#Conv3
x = Conv2D(filters=nFiltersPerStep, kernel_size=3, strides=1, padding='same')(x)
#x = Activation('relu')(x)
x = Conv2D(filters=nFiltersPerStep, kernel_size=3, strides=1, padding='same')(x)
x = BatchNormalization()(x)
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
x = Dropout(0.5)(x)
x = Flatten()(x)
predictions = Dense(num_classes, activation='sigmoid')(x)
model2 = Model(inputs=inputs, outputs=predictions)

model2.summary()

model2.compile(loss='categorical_crossentropy',
               optimizer=Adam(lr=0.001),
               metrics=['accuracy'])

# return value each epochs
hist = model2.fit(x_train, y_train,
                  batch_size=batch_size,
                  epochs=epochs,
                  verbose=1,
                  validation_split=0.05)

# evaluate model
score = model2.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

predictions = model2.predict(x_test)
combinations = np.c_[y_label, predictions]

total_time = time.time() - start
print('Total time:', format(total_time) + '[sec]')

# outputs
outputpath = 'result/cnn/' + date
os.makedirs(outputpath)
otp.ModelOutput(model2, outputpath)
otp.EvaluateOutput(score, outputpath)
otp.CsvOutput(combinations, outputpath)
otp.TotalTimeOutput(total_time, outputpath)
gpt.loss_and_acc(hist, epochs, outputpath)
