# correction_horizontale.py : 
# -*-coding:Latin-1 -*

# imports
from time import sleep
import numpy as np
import cv2

retour = 270

def correction_value(x,w,x_middle):
    correction = 0
    mw = w/2
    middle_target = x+int(mw)
    diff = x_middle - middle_target
    print('diff = ' + str(diff))
    if diff > 15:
        correction -= 5
    if diff < -15:
        correction += 5
    return correction

def correction_horizontale(im,x,w):
    format = np.shape(im)
    x_middle = format[0]/2
    x_middle = int(x_middle)
    angle = get_angle()
    if correction_value(x,w,x_middle) != 0:
        print('Correction necessaire ...')
        new_angle = angle + correction_value(x,w,x_middle)
        print('Nouvel angle : ' + str(new_angle))
        p = False
        return new_angle, p
    else:
        print('Correction non necessaire ...')
        print('Arret de la correction')
        p = True
        return angle, p

def set_angle(a):
    global retour
    retour = a

def get_angle():
    global retour
    return retour
    