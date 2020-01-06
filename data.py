
import cv2
import numpy as np
import matplotlib.pyplot as plt

import glob
import numpy as np
import random
import pandas as pd
import math

kernel = np.ones((5, 5), np.uint8);

def load_pc(data_path):
    path_list = glob.glob('C:/Users/admin/Desktop/MachineLearning/Miniproject/RawData2/'+data_path+'/*')
    file_list = [None for i in range(len(path_list))]
    
    for i in range(len(path_list)):
        file_list[i] = cv2.imread(path_list[i])
        file_list[i] = cv2.resize(file_list[i],None, fx=0.1, fy=0.1)

        #Hair removal (Use the opencv to do morphological treatment / closing, erosion,...)
        img_blue_c1, img_green_c1, img_red_c1 = cv2.split(file_list[i])
        img_green_c1 = cv2.morphologyEx(img_green_c1, cv2.MORPH_CLOSE, kernel)
        img_red_c1 = cv2.morphologyEx(img_red_c1, cv2.MORPH_CLOSE, kernel)
        file_list[i]=cv2.merge((img_blue_c1, img_green_c1, img_red_c1))

    return file_list

def random(file_list):

    file_np = np.array(file_list)
    indices = np.arange(len(file_list))

    
    np.random.shuffle(indices)
    file_list = file_np[indices]

    return file_list