# detection_pointeur.py : 
# -*-coding:Latin-1 -*
# programme de detection de pointeur : reçoit une image, en déduit la position du pointeur sur l'image, renvoie cette position

# imports
import matplotlib.pyplot as plt
import matplotlib.image as pim
import numpy as np
import cv2
from time import sleep

# fonctions

# fonction tout ou rien, renvoie l'image en binaire, pointeur en blanc, le reste en noir
def TOR_Pointeur(img):  # a, b, c, d : tolerance en RGBA
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

# la fonction suivante renvoie true si au moins un pixel blanc (du pointeur) est repéré, false sinon
def check_if_pixel_blanc(img):
    ret = False
    format = np.shape(img)
    for i in range(format[0]):
        for j in range(format[1]):
            if img[i,j] == 255:
                ret = True
    return ret

# la fonction suivante renvoie la position du pixel au centre du pointeur
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

# main
def main_detection(img):
    
    # processing et affichage console
    ret = -1
    print('Demarrage du programme de detection de pointeur --------')
    sleep(0.5) # /!\ sleep
    print('Traitement : ')
    sleep(0.5) # /!\ sleep
    processed_img = TOR_Pointeur(img)
    print('\t Lecture reussie')
    sleep(0.5) # /!\ sleep
    print('\t TOR reussi')
    sleep(0.5) # /!\ sleep
    detection = check_if_pixel_blanc(processed_img)
    if detection:
        print('\t Pointeur repere')
        sleep(0.5) # /!\ sleep
        center = get_pointeur_position(img)
        print('\t Position du centre : (' + str(center[0])+','+str(center[1])+')')
        sleep(0.5) # /!\ sleep
        print('\t Affichage')
        sleep(0.5) # /!\ sleep
        print('Fin du Traitement')
        
    else :
        print('\t Pointeur non reperee')
        sleep(0.5) # /!\ sleep
        print('Arret du programme de detection')
        sleep(0.5) # /!\ sleep
        
    # affichage images
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.namedWindow('processed_img', cv2.WINDOW_NORMAL)
    cv2.imshow('img',img)
    cv2.imshow('processed_img',processed_img)
    return center

# execution
img_path = r"C:\Users\raph-\Desktop\Travail\4A\Majeure Image\Projet Transversal\Traitement d'image\jalon_2\img\img_test_4.png"
im = cv2.imread(img_path,0)
main_detection(im)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('Arret du programme de detection de pointeur -------------')