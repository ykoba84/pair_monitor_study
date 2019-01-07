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

# my liblaries
import dataset as ds
import graph_plot as gpt
import outputs as otp
    
start = time.time()
date = datetime.now().strftime("%y%m%d_%H%M%S")
print("time stamp :", date)

batch_size = 25
num_class_xlabels = 10
num_class_ylabels = 10
epochs = 100

print("hyper parameteres : batch_size=", batch_size, "epochs=", epochs)

# make train_data
x_train, y_train, z_train = ds.read_2para_xlabels10_ylabels10("train_data_2para_xlabels10_ylabels10")

# make val_data
x_val, y_val, z_val = ds.read_2para_xlabels10_ylabels10("test_data_2para_xlabels10_ylabels10")

# change list to array
#x_train = np.array(x_train)
#x_val = np.array(x_val)

# reshape
x_train = x_train.reshape(x_train.shape[0], 80, 80, 1)
x_val = x_val.reshape(x_val.shape[0], 80, 80, 1)

# predict
y_label = np.array(y_val)
z_label = np.array(z_val)

# change list to categorical
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)
z_train = to_categorical(z_train)
z_val = to_categorical(z_val)

#print(y_train.shape)

# set loss
imagedim = (80,80,1)

##### input #####
inputs = Input( shape=imagedim )
ksize = 5

##### conv1 #####
x = Conv2D(filters=128, kernel_size=ksize, strides=1, padding='same' )(inputs)
x = BatchNormalization()(x)
x = Activation('relu')(x)
x = Conv2D(filters=128, kernel_size=ksize, strides=1, padding='same' )(x)
x = BatchNormalization()(x)
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
x = Dropout(0.25)(x)

##### conv2 #####
x = Conv2D(filters=256, kernel_size=ksize, strides=1, padding='same' )(x)
x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=256, kernel_size=ksize, strides=1, padding='same' )(x)
x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
x = Dropout(0.25)(x)
"""
##### conv3 #####
x = Conv2D(filters=256, kernel_size=ksize, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=256, kernel_size=ksize, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)

##### conv4 #####
x = Conv2D(filters=512, kernel_size=ksize, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=512, kernel_size=ksize, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)

##### conv5 #####
x = Conv2D(filters=512, kernel_size=ksize, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Conv2D(filters=512, kernel_size=ksize, strides=1, padding='same' )(x)
#x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = MaxPooling2D(2)(x)
"""
##### fully-connected layers #####
x = Flatten()(x)
x = Dense(100)(x)
x = BatchNormalization()(x)        
x = Activation('relu')(x)
x = Dropout(0.5)(x)
#x = Dense(1024)(x)
#x = Activation('relu')(x)
#x = Dropout(0.5)(x)

output1 = Dense(num_class_xlabels, activation='softmax', name='output_sigmax')(x)
output2 = Dense(num_class_ylabels, activation='softmax', name='output_sigmay')(x)

model2 = Model(inputs=inputs, outputs=[output1, output2])

model2.summary()

model2.compile(loss={'output_sigmax':'categorical_crossentropy',
                     'output_sigmay':'categorical_crossentropy'},
               optimizer=Adam(lr=0.001),
               metrics=['accuracy'])

# return value each epochs
hist = model2.fit(x_train, {'output_sigmax':y_train,
                            'output_sigmay':z_train},
                  batch_size=batch_size,
                  epochs=epochs,
                  verbose=2,
                  validation_split=0.1)

# evaluate model
score = model2.evaluate(x_val,
                        {'output_sigmax':y_val,
                         'output_sigmay':z_val},
                        verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])

predictions = model2.predict(x_val)

combinations_sigmax = np.c_[y_label, predictions[0]]
combinations_sigmay = np.c_[z_label, predictions[1]]

total_time = time.time() - start
print('Total time:', format(total_time) + '[sec]')

# outputs
outputpath = 'result/cnn/' + date
os.makedirs(outputpath)
otp.ModelOutput(model2, outputpath)
otp.EvaluateOutput(score, outputpath)
otp.CsvOutput_2para('x', combinations_sigmax, outputpath)
otp.CsvOutput_2para('y', combinations_sigmay, outputpath)
otp.TotalTimeOutput(total_time, outputpath)
otp.HyperParameterOutput(batch_size, outputpath)
gpt.loss_and_acc_2para(hist, epochs, outputpath)

