    # Fichier permettant le traitement des images recues depuis le Rasberry

# Import des librairies
import matplotlib.pyplot as mplot
import numpy as np

# Fonctions de traitement :

# Processing : Recupere une image, applique un K-means
def Processing(img):
    exit(0)
    
    

# Recuperation de l'image
# Je pars du principe qu'on recupere les images dans un dossier qui s'actualise au fur et a mesure de la reception

# Nombre d'image que peut contenir le dossier au max :
nb_img = 5
# Frequence de recuperation des images ?

#while(True):
for k in range(nb_img):
    img = mplot.imread('images/image_'+str(k+1)+'.png')
    format = np.shape(img)
    new_img=np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i,j,0]
            img_G = img[i,i,1]
            img_B = img[i,j,2]
            img_I = img[i,i,3]
            if (img_R<0.5) & (img_G<0.5) & (img_B>0.8) & (img_I>0.2):
                new_img[i,j,3] = 0
            else:
                new_img[i,j,3] = 1
mplot.imshow(new_img)
mplot.axis('off')
mplot.show()