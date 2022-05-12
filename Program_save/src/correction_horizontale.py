# correction_horizontale.py : 
# -*-coding:Latin-1 -*

# imports
from time import sleep
import numpy as np
import cv2

retour = 270
WIDTH_FRAME = 512

def correction_value(x,w):
    correction = 0
    mw = w/2
    middle_target = x+int(mw)
    diff = int(WIDTH_FRAME/2) - middle_target
    print("YOOOOOOOOOOOOOOOOOOOOOY" + str(diff), int(WIDTH_FRAME/2))
    tolerance = 7
    if diff > tolerance:
        correction += 2
    if diff < -1*tolerance:
        correction -= 2
    return correction

def correction_horizontale(im,x,w):

    angle = get_angle()
    if correction_value(x,w) != 0:
        print('Correction necessaire ...')
        new_angle = angle + correction_value(x,w)
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
    