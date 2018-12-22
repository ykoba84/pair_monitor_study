import numpy as np
from PIL import Image
from tqdm import tqdm
import os

def read_data(dataPath):

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

        # Convert the image to a 64 x 64 pixel and read as a 64 x 64 two-dimensional array of elements with one element containing [R, G, B] 3 elements.
        image = np.array(Image.open(fname).convert('L').resize((64, 64)))
        # Convert the array to a form like [[Red], [Green], [Blue]].
        #image = image.transpose()
        # Convert to a flat one-dimensional array.
        # Elements of the first one third are red, the next is green, and the last is blue.
        #image = image.reshape(image.shape[0], image.shape[1]).astype("float32")[0]
        image = image.reshape(1, image.shape[0] * image.shape[1]).astype("float32")[0]
        #image = image.astype("float32")

        image_list.append(image / 255.)

        #print(fname)
        #print(sigma)

    return image_list, label_list

def read_0238(dataPath):

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

        # Convert the image to a 64 x 64 pixel and read as a 64 x 64 two-dimensional array of elements with one element containing [R, G, B] 3 elements.
        image = np.array(Image.open(fname).convert('L').resize((64, 64)))
        # Convert the array to a form like [[Red], [Green], [Blue]].
        #image = image.transpose()
        # Convert to a flat one-dimensional array.
        # Elements of the first one third are red, the next is green, and the last is blue.
        #image = image.reshape(image.shape[0], image.shape[1]).astype("float32")[0]
        image = image.reshape(1, image.shape[0] * image.shape[1]).astype("float32")[0]
        #image = image.astype("float32")

        image_list.append(image / 255.)

        #print(fname)
        #print(sigma)

    return image_list, label_list

def read_detail(dataPath):

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
        sigma = float(file[m-3:m])

        # read label
        if sigma == 0.8:
            label = 0
        elif sigma == 1.0:
            label = 1
        elif sigma == 1.2:
            label =2 
        elif sigma == 1.4:
            label = 3
        elif sigma == 1.6:
            label = 4
        elif sigma == 1.8:
            label = 5
        elif sigma == 2.0:
            label = 6
        elif sigma == 2.2:
            label = 7
        elif sigma == 2.4:
            label = 8
        elif sigma == 2.6:
            label = 9
        elif sigma == 2.8:
            label = 10
        elif sigma == 3.0:
            label = 11
        

        label_list.append(label)

        # Convert the image to a 64 x 64 pixel and read as a 64 x 64 two-dimensional array of elements with one element containing [R, G, B] 3 elements.
        image = np.array(Image.open(fname).convert('L').resize((64, 64)))
        # Convert the array to a form like [[Red], [Green], [Blue]].
        #image = image.transpose()
        # Convert to a flat one-dimensional array.
        # Elements of the first one third are red, the next is green, and the last is blue.
        #image = image.reshape(image.shape[0], image.shape[1]).astype("float32")[0]
        image = image.reshape(1, image.shape[0] * image.shape[1]).astype("float32")[0]
        #image = image.astype("float32")

        image_list.append(image / 255.)

        #print(fname)
        #print(sigma)

    return image_list, label_list

def read_2para_xlabels10_ylabels10(dataPath):

    # make dataset list
    image_list = []
    label1_list = []
    label2_list = []

    # debug
    nfile=0
    
    for file in tqdm(os.listdir(dataPath)):

        # debug
        
        nfile=nfile+1
        if nfile>10:
            break
        
        
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

        # debug
        #print("File name is ", file, " sigma x = ", sigmax, " sigma y = ", sigmay, " label1 : ", label1, " label2 : ", label2)
        

        label1_list.append(label1)
        label2_list.append(label2)

        # Convert the image to a 64 x 64 pixel and read as a 64 x 64 two-dimensional array of elements with one element containing [R, G, B] 3 elements.
        image = np.array(Image.open(fname).convert('L').resize((64, 64)))
        
        # Convert the array to a form like [[Red], [Green], [Blue]].
        #image = image.transpose()
        
        # Convert to a flat one-dimensional array.
        # Elements of the first one third are red, the next is green, and the last is blue.
        image = image.reshape(1, image.shape[0] * image.shape[1]).astype("float32")[0]

        # normalize
        image_list.append(image / 255.)

        #print(fname)
        #print(sigma)

    return image_list, label1_list, label2_list
