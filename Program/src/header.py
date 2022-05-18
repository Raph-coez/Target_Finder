# header.py
# contient toutes les fonctions utilisees dans main.py



# imports

from matplotlib.pyplot import gray
from time import sleep
from imutils.video import VideoStream
import numpy as np
import argparse
import serial
import cv2
import os
from math import exp,log

# variables gloables
WIDTH_FRAME = 512
PROCESSED = False
COUNT = 0
SEARCHING_TARGET = True
LUMIERE_TRUE = "L"
LUMIERE_FALSE = "E"
DATA = [0,0,0,0]
ANGLE = 278
ANGLE_VERTICAL = 160


# fonctions

def vertical_correction_value(pos,y,h):
    correction = 0
    mh = h/2
    middle_target = y + int(mh)
    diff =  middle_target - int(pos[1])
    tolerance = 7
    if diff > tolerance:
        correction += 2 
    if diff < -1*tolerance:
        correction -= 2
    return correction

def horizontal_correction_value(x,w):
    correction = 0
    mw = w/2
    middle_target = x+int(mw)
    diff = int(WIDTH_FRAME/2) - middle_target
    tolerance = 7
    if diff > tolerance:
        correction += 2
    if diff < -1*tolerance:
        correction -= 2
    return correction

def correction_verticale(pointeur_pos,y,h):
    angle = ANGLE_VERTICAL
    if vertical_correction_value(y,h) != 0:
        print('Correction verticale necessaire ...')
        new_angle = angle + vertical_correction_value(pointeur_pos,y,h)
        print('Nouvel angle vertical : ' + str(new_angle))
        p = False
        return new_angle, p
    else:
        print('Correction non necessaire ...')
        print('Arret de la correction')
        p = True
        return angle, p
    
def correction_horizontale(im,x,w):

    angle = ANGLE
    if horizontal_correction_value(x,w) != 0:
        print('Correction necessaire ...')
        new_angle = angle + horizontal_correction_value(x,w)
        print('Nouvel angle : ' + str(new_angle))
        p = False
        return new_angle, p
    else:
        print('Correction non necessaire ...')
        print('Arret de la correction')
        p = True
        return angle, p

def get_detector():
    print("Démarrage du programme ...")
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--cascade", type=str, help = "path to input directory containing haar cascades", default="..\data\cascade.xml")
    args = vars(ap.parse_args())
    detector = cv2.CascadeClassifier(args["cascade"])
    return detector

def init_position(ser,consigne_init,msg):
    for i in consigne_init:
        ser.write(i.encode())
    print(msg)
    
def print_camera(vs):
    frame = vs.read()
    frame = cv2.resize(frame, (512, 384))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('..\img\img.png',frame)
    return gray, frame

def check_detection(detector, gray_img):
    rect = detector.detectMultiScale( gray_img, scaleFactor=1.25, minNeighbors=1, minSize=(5, 5), flags=cv2.CASCADE_SCALE_IMAGE)
    if rect == ():
        detected = False
        if COUNT%100 == 0:
            print('Pas de cible')
    else : 
        detected = True
        if COUNT%100 == 0:
            print('Cible detectee')
    return detected, rect

def set_data(rect,frame):
    for (fX, fY, fW, fH) in rect:
        DATA = [fX,fW,fY,fH]
        cv2.rectangle(frame, (fX, fY), (fX + fW, fY + fH), (0, 0, 255), 2)
        distance = int(13315*exp(-0.986*log(fH)))
        return distance

def vertical_target(pointeur_pos, detect, ser):
    if (detect):
        sleep(0.1)
        im = cv2.imread('..\img\img.png',0)
        y,h = DATA[2],DATA[3]
        angle, PROCESSED = correction_verticale(pointeur_pos,y,h)
        consigne = str(angle) + 'F'
        ser.write(consigne.encode())
        if PROCESSED:
            print('Cible atteinte ***********')
            print('Arret de la correction')
            ser.write(LUMIERE_FALSE.encode())
            sleep(0.5)
            ser.write(LUMIERE_TRUE.encode())
            SEARCHING_TARGET = False
        else:
            if (angle < 3 or angle > 176):
                print('Angle maximal atteint')
            else:
                ANGLE = angle
                print('Angle modifé : ' + str(angle))
            
def horizontal_target(detected,ser):
    if(detected):
        sleep(0.1)
        im = cv2.imread('..\img\img.png',0)
        x,w = DATA[0],DATA[1]
        angle, PROCESSED = correction_horizontale(im,x,w)
        consigne = str(angle) + 'F'
        ser.write(consigne.encode())
        if PROCESSED:
            print('Position horizontale atteinte')
            print("Arret de la correction d'angle horizontal")
            ser.write(LUMIERE_TRUE.encode())
        else:
            if (angle < 183 or angle > 356):
                print('Angle maximal atteint')
            else:
                ANGLE = angle
                print('Angle modifé : ' + str(angle))

def TOR_Pointeur(img): 
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            gray_pixel = img[i, j]
            if ((gray_pixel < 250)):
                new_img[i, j] = 0
            else:
                new_img[i, j] = 255
    form_2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
    new_img = cv2.morphologyEx(new_img,cv2.MORPH_CLOSE,form_2)
    return new_img

def check_if_pixel_blanc(img):
    ret = False
    format = np.shape(img)
    for i in range(format[0]):
        for j in range(format[1]):
            if img[i,j] == 255:
                ret = True
    return ret

def get_pointeur_position(img):
    center = (0,0)
    bords = []
    first = True
    second = True
    format = np.shape(img)
    for i in range(format[0]):
        for j in range(format[1]):
                if (img[i,j] == 255 and first):
                    bords.append([i,j])
                    first = False
                    break
    for i in range(format[0]):
        for j in range(format[1]):
            if (img[format[0]-i-1,j] == 255 and second):
                bords.append([format[0]-i-1,j])
                second = False
                break  
    if(not first and not second):
        middle = (bords[1][0]-bords[0][0])/2 + bords[0][0]
        center = (int(middle),bords[0][1])
    return center       

def get_pointeur_center(img):
    
    # processing et affichage console
    print('Demarrage du programme de detection de pointeur --------')
    processed_img = TOR_Pointeur(img)
    detect = check_if_pixel_blanc(processed_img)
    if detect:
        print('\t Pointeur repere')
        center = get_pointeur_position(img)
        print('Arret du programme de detection de pointeur -------------')
        
    else :
        print('\t Pointeur non reperee')
        print('Arret du programme de detection de pointeur -------------')
        
    # affichage images
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.namedWindow('processed_img', cv2.WINDOW_NORMAL)
    cv2.imshow('img',img)
    cv2.imshow('processed_img',processed_img)
    return center, detect