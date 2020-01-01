import numpy as np
import cv2
from PIL import Image
from tqdm import tqdm
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import os
from multiprocessing import Pool

def load_img_pil(filename, img_size):

    img = np.array(Image.open(filename).resize((img_size,img_size)).convert('L'))
    converted_img = img.flatten().astype("float32")
    return converted_img

def load_img_cv2(filename, img_size):

    # read images in grayscale
    img = cv2.imread(filename, 0)
    # resize to 64x64 from 80x80
    img = cv2.resize(img, dsize=(img_size, img_size))
    # Convert to a flat one-dimensional array.
    img = img.reshape(1, img.shape[0] * img.shape[1]).astype("float32")[0]

    return img

def load_img_keras(filename, img_size):

    img = load_img(filename, color_mode="grayscale", target_size=(img_size, img_size))
    img_array = img_to_array(img) / 255.
    img_array = img_array.flatten()
    return img_array

def read_data_sigmay_of_ebunch(dataPath):

    # make dataset list
    image_list = []
    label_list = []
    nfile=0
    for file in tqdm(os.listdir(dataPath)):
        """
        nfile=nfile+1
        if nfile>100:
            break
        """
        fname = dataPath + '/' + file
        label = 0

        m = file.find('-')
        sigma = int(file[m-2:m])

        # read label
        if sigma == 1:
            label = 0
        elif sigma == 2:
            label = 1
        elif sigma == 3:
            label =2 
        elif sigma == 4:
            label = 3
        elif sigma == 5:
            label = 4
        elif sigma == 6:
            label = 5
        elif sigma == 7:
            label = 6
        elif sigma == 8:
            label = 7
        elif sigma == 9:
            label = 8
        elif sigma == 10:
            label = 9

        label_list.append(label)

        image = load_img_pil(fname, 64)
        image_list.append(image / 255.)

    return image_list, label_list

def read_data_sigmay(dataPath):

    # make dataset list
    image_list = []
    label_list = []
    nfile=0
    for file in tqdm(os.listdir(dataPath)):
        
        nfile=nfile+1
        if nfile>1000:
            break
        
        fname = dataPath + '/' + file
        label = 0

        m = file.find('-')
        sigma = float(file[m-3:m])

        # read label
        if sigma == 0.2:
            label = 0
        elif sigma == 0.4:
            label = 1
        elif sigma == 0.6:
            label = 2
        elif sigma == 0.8:
            label = 3
        elif sigma == 1.0:
            label = 4
        elif sigma == 1.2:
            label = 5
        elif sigma == 1.4:
            label = 6
        elif sigma == 1.6:
            label = 7
        elif sigma == 1.8:
            label = 8
        elif sigma == 2.0:
            label = 9
        elif sigma == 2.2:
            label = 10
        elif sigma == 2.4:
            label = 11
        elif sigma == 2.6:
            label = 12
        elif sigma == 2.8:
            label = 13
        elif sigma == 3.0:
            label = 14
        elif sigma == 3.2:
            label = 15
        elif sigma == 3.4:
            label = 16
        elif sigma == 3.6:
            label = 17
        elif sigma == 3.8:
            label = 18

        label_list.append(label)

        image = load_img_cv2(fname, 64)

        image_list.append(image / 255.)

        #print(fname)
        #print(sigma)

    return image_list, label_list

def read_2para_xlabels10_ylabels10(dataPath):

    # make dataset nparray
    image_array = np.empty(0)
    image_list = []
    label1_list = []
    label2_list = []

    counter = 0

    # debug
    nfile=0
    
    for file in tqdm(os.listdir(dataPath)):

        # debug
        """
        nfile=nfile+1
        if nfile>20000:
            break
        """
        """
        if counter == 0:
            image_list = []
        """
        fname = dataPath + '/' + file
        label = 0

        x_check_point = file.find('x')
        y_check_point = file.find('y')

        sigmax = float(file[x_check_point+1:x_check_point+4])
        sigmay = float(file[y_check_point+1:y_check_point+4])

        # read sigmax
        if sigmax == 0.2:
            label1 = 0
        elif sigmax == 0.4:
            label1 = 1
        elif sigmax == 0.6:
            label1 = 2
        elif sigmax == 0.8:
            label1 = 3
        elif sigmax == 1.0:
            label1 = 4
        elif sigmax == 1.2:
            label1 = 5
        elif sigmax == 1.4:
            label1 = 6
        elif sigmax == 1.6:
            label1 = 7
        elif sigmax == 1.8:
            label1 = 8
        elif sigmax == 2.0:
            label1 = 9
        
        # read sigmay
        if sigmay == 0.2:
            label2 = 0
        elif sigmay == 0.4:
            label2 = 1
        elif sigmay == 0.6:
            label2 = 2
        elif sigmay == 0.8:
            label2 = 3
        elif sigmay == 1.0:
            label2 = 4
        elif sigmay == 1.2:
            label2 = 5
        elif sigmay == 1.4:
            label2 = 6
        elif sigmay == 1.6:
            label2 = 7
        elif sigmay == 1.8:
            label2 = 8
        elif sigmay == 2.0:
            label2 = 9

        #image = img_open_from_files(fname, 80)
        image = load_img_cv2(fname, 40)

        image_list.append(image / 255.)
        label1_list.append(label1)
        label2_list.append(label2)
        """
        if counter == 10000:
            image_array = np.append(image_array, np.asarray(image_list))
            counter = 0
            continue
        
        counter += 1
        """
    image_array = np.array(image_list, dtype=np.float32)
    #image_array = np.append(image_array, np.asarray(image_list))

    return image_array, label1_list, label2_list

# Multiprocessing
def load_img_data(filename, dataPath):
    
    fname = dataPath + '/' + filename
    label = 0

    x_check_point = filename.find('x')
    y_check_point = filename.find('y')

    sigmax = float(filename[x_check_point+1:x_check_point+4])
    sigmay = float(filename[y_check_point+1:y_check_point+4])

    # read sigmax
    if sigmax == 0.2:
        label1 = 0
    elif sigmax == 0.4:
        label1 = 1
    elif sigmax == 0.6:
        label1 = 2
    elif sigmax == 0.8:
        label1 = 3
    elif sigmax == 1.0:
        label1 = 4
    elif sigmax == 1.2:
        label1 = 5
    elif sigmax == 1.4:
        label1 = 6
    elif sigmax == 1.6:
        label1 = 7
    elif sigmax == 1.8:
        label1 = 8
    elif sigmax == 2.0:
        label1 = 9
            
    # read sigmay
    if sigmay == 0.2:
        label2 = 0
    elif sigmay == 0.4:
        label2 = 1
    elif sigmay == 0.6:
        label2 = 2
    elif sigmay == 0.8:
        label2 = 3
    elif sigmay == 1.0:
        label2 = 4
    elif sigmay == 1.2:
        label2 = 5
    elif sigmay == 1.4:
        label2 = 6
    elif sigmay == 1.6:
        label2 = 7
    elif sigmay == 1.8:
        label2 = 8
    elif sigmay == 2.0:
        label2 = 9

    #image = img_open_from_files(fname, 80)
    image = load_img_cv2(fname, 80)

    return image, label1, label2

def wrapper(args):

    return load_img_data(*args)

def read_2para_xlabels10_ylabels10_multiprocessing(dataPath):

    # make dataset nparray
    image_array = np.empty(0)
    image_list = image_array.tolist()
    label1_list = []
    label2_list = []

    # debug
    nfile=0

    filelist = [(file, dataPath) for file in os.listdir(dataPath)]

    p = Pool(6)

    counter = 0
    parts = 0
    for image_temp, label1_temp, label2_temp in p.map(wrapper, filelist):
        image_list.append(image_temp)
        label1_list.append(label1_temp)
        label2_list.append(label2_temp)
        
    image_array = np.array(image_list)

    p.close()

    return image_array, label1_list, label2_list
