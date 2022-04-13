    # Fichier permettant le traitement des images recues depuis le Rasberry

# Import des librairies / algos
import matplotlib.pyplot as plt
import matplotlib.image as pim
import numpy as np
import cv2
from algos import *

# Processing : choix de la methode de traitement
def Processing(img):
    return TOR(img)

def check_prop(prop):
    ret = ""
    print(prop)
    if prop > 0.001:
        ret = "Cible reperee"
    else:
        ret = "Pas de cible"
    return ret
        

# Periode de recuperation des images (ms)
T = 20

# Camera
cam = cv2.VideoCapture(0)
plt.figure(1)

# Boucle d'affichage
while True:
    ret, img = cam.read()
    if ret:
        copy_image = np.copy(img)
        pim.imsave('images/cam.png', img)
        img = plt.imread('images/cam.png')
        processed_img, prop = Processing(img)
        plt.subplot(121)
        plt.imshow(img)
        plt.title('Image non traitee')
        plt.axis('off')
        plt.subplot(122)
        plt.imshow(processed_img)
        plt.title(check_prop(prop))
        plt.axis('off')
        plt.show(False)
        plt.pause(2)
        plt.close()
        if cv2.waitKey(T) & 0xFF == ord('q'):
            break
    else:
        print('Aucun retour camera')
        break
