import os
from tensorflow.keras.preprocessing.image import load_img, img_to_array, smart_resize
import numpy as np
import pathlib
from pathlib import Path
import json


def image_load():

    data_dir = "C:/Users/keevv/Desktop/Roll_Off/waste"
    p = Path().cwd()
    q = p/'waste'
    images = []
    labels = []
    for folder in q.iterdir():
        current_label = folder.name
        for img in folder.iterdir():
            img = load_img(img, grayscale = True)
            img_array = img_to_array(img)/255
            size = (180, 320)
            image_array_resized = smart_resize(img_array, size)
            images.append(image_array_resized)
            labels.append(current_label)
    return np.array(images), np.array(labels)



def test_loader(test_file):


    data_directory = test_file
    p_1 = Path().cwd()
    q_1 =  p_1/data_directory             ## The file has to be in the same folder and the name of the test file has to be named as test
    ip_images = []
    ip_im_name = []

    for img in q_1.iterdir():
        if(str(img).find('.jpg')>0):
            ip_im_name_now = img
            img = load_img(img, grayscale = True)
            img_array = img_to_array(img)/255
            size = (180,320)
            img_array_resized = smart_resize(img_array,size)
            ip_images.append(img_array_resized)
            ip_im_name.append(ip_im_name_now)
        else:
            with open(img, 'r') as f:
                speed_data = json.load(f)
    return np.array(ip_images), ip_im_name, speed_data


def timestamps(ip_pred, ip_im_name, speed_data ):
    ip_pred_norm = []
    ip_out = []
    ts = []
    speed = []
    n1 = 0

    for ip_y in ip_pred:
        ip_pred_norm.append(np.argmax(ip_y))
    for i in ip_im_name:
        nw = str(i)
        ts.append(str(i)[nw.find('T')-8:nw.find('T')+7])
        nw = str(i)
    for i in ts:
        for j in speed_data:
            if(i==str(j)[str(j).find('Filename')+12:str(j).find('.jpg')-3]):
                speed.append(j['Speed'])
                break    
    for y,name,ts,s in zip(ip_pred_norm,ip_im_name,ts,speed):
        now = y,ts,str(name),s
        ip_out.append(now)
        dt = {'names':['Pred', 'TS', 'Name' ,'Speed'],'formats':[int, object, object,float]}
        Y = np.array(ip_out, dtype=dt)
        Y = np.sort(Y, order='TS')
    return Y





