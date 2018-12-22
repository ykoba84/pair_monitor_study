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
num_classes = 19
kernel_size = 4
epochs = 100

print("hyper parameteres : batch_size=", batch_size, " epochs=", epochs, " kernel_size=", kernel_size)

# make train_data
#x_train, y_train = ds.read_data("train_data_100000")
#x_train, y_train = ds.read_detail("train_data_pBunch")
x_train, y_train = ds.read_0238("train_data_0238")
# make val_data
#x_val, y_val = ds.read_data("test_data_5000")
#x_val, y_val = ds.read_detail("test_data_detail")
x_val, y_val = ds.read_0238("test_data_0238")

# change list to array
x_train = np.array(x_train)
x_val = np.array(x_val)

# reshape
x_train = x_train.reshape(x_train.shape[0], 64, 64, 1)
x_val = x_val.reshape(x_val.shape[0], 64, 64, 1)

# predict
y_label = np.array(y_val)

# change list to categorical
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)

#print(y_train.shape)

# set loss
imagedim = (64,64,1)

##### input #####
inputs = Input( shape=imagedim )

##### conv1 #####
x = Conv2D(filters=64, kernel_size=kernel_size, strides=1, padding='same' )(inputs)
#x = BatchNormalization()(x)
x = Activation('relu')(x)
x = Conv2D(filters=64, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
x = Dropout(0.25)(x)

##### conv2 #####
x = Conv2D(filters=128, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=128, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
x = Dropout(0.25)(x)

"""
##### conv3 #####
x = Conv2D(filters=256, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=256, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)

##### conv4 #####
x = Conv2D(filters=512, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=512, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)

##### conv5 #####
x = Conv2D(filters=512, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=512, kernel_size=kernel_size, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
"""
##### fully-connected layers #####
x = Flatten()(x)
x = Dense(1024)(x)
x = Activation('relu')(x)
x = Dropout(0.5)(x)
#x = Dense(1024)(x)
#x = Activation('relu')(x)
#x = Dropout(0.5)(x)
predictions = Dense(num_classes, activation='softmax')(x)
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
                  validation_split=0.2)
#                  validation_data=(x_val, y_val))

# evaluate model
score = model2.evaluate(x_val, y_val, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

predictions = model2.predict(x_val)
combinations = np.c_[y_label, predictions]

total_time = time.time() - start
print('Total time:', format(total_time) + '[sec]')

# outputs
outputpath = 'result/cnn/' + date
os.makedirs(outputpath)
otp.ModelOutput(model2, outputpath)
otp.EvaluateOutput(score, outputpath)
otp.CsvOutput_0238(combinations, outputpath)
otp.TotalTimeOutput(total_time, outputpath)
otp.HyperParameterOutput(batch_size, outputpath)
gpt.loss_and_acc(hist, epochs, outputpath)

