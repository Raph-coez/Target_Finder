    # Fichier permettant le traitement des images recues depuis le Rasberry

# Import des librairies
import matplotlib.image as mpimg
import matplotlib.pyplot as mplot
import numpy as np
import PIL.Image as pim

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
    img = mpimg.imread('images/image_'+str(k+1)+'.png')
    img = np.asarray(pim.open('images/image_'+str(k+1)+'.png'))
    img = 255 * img
    print(img)
    print(img[34,100,1])
    format = np.shape(img)
    new_img=np.empty((format[0],format[1]))
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i,j,0]
            img_G = img[i,i,1]
            img_B = img[i,j,2]
            img_I = img[i,i,3]
            #if (img_R>100) & (img_G>100) & (img_B<250) & (img_I<100)
    
        # Traitement : 
    
        #mplot.imshow(img)
        #mplot.show()