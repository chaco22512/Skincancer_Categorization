#!/usr/bin/env python
# coding: utf-8

# In[2]:


import glob
import cv2
import numpy as np
import random
import pandas as pd


# In[3]:


def load_pc(data_path):
    path_list = glob.glob('Desktop/Python/Miniproject/RawData/'+data_path+'/*')
    file_list = [None for i in range(len(path_list))]
    
    for i in range(len(path_list)):
        file_list[i] = cv2.imread(path_list[i])
        file_list[i] = cv2.cvtColor(file_list[i], cv2.COLOR_BGR2RGB)
        file_list[i] = cv2.resize(file_list[i], (255,255))
    
    file_np = np.array(file_list)
    
    indices = np.arange(len(path_list))
    np.random.shuffle(indices)
    file_list = file_np[indices]
    
    return file_list

