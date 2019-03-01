from tqdm import tqdm
import os

label_list = [[0 for i in range(10)] for j in range(10)]

for file in tqdm(os.listdir("train_data_2para_x0220y0220")):
    
    x_check_point = file.find('x')
    y_check_point = file.find('y')

    sigmax = float(file[x_check_point+1:x_check_point+4])
    sigmay = float(file[y_check_point+1:y_check_point+4])

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

    label_list[label1][label2] += 1

for i in range(10):
    for j in range(10):
        print(label_list[i][j], " ", end="")
    print(" ")
