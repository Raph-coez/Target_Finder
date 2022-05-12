import matplotlib.pyplot as mplot
import numpy as np
import cv2

def TOR_blue(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R < 0.5) and (img_G < 0.5) and (img_B > 0) and (img_I > 0.2)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img


    # TOR_cyan
def TOR_cyan(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R < 0.5) and (img_G < 1) and (img_B > 0.5) and (img_I > 0.8)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img



    # TOR_magenta
def TOR_magenta(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R > 0.5) and (img_G < 0.3) and (img_B > 0.5) and (img_I > 0.8)):
                new_img[i, j, 3] = 0
            else:
                new_img[i, j, 3] = 1
    return new_img

def TOR(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    taille = format[0] * format[1]
    count = 0
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R > 0) and (img_G < 0.3) and (img_B > 0.4) and (img_I > 0.0)):
                new_img[i, j, 3] = 0
                count += 1
            else:
                new_img[i, j, 3] = 1
    if (count > 0):
        proportion = taille/count
    else:
        proportion = taille
    return new_img, proportion


def TOR_A(img):  # a, b, c, d : tolerance en RGBA
    format = np.shape(img)
    new_img = np.empty(format)
    taille = format[0] * format[1]
    count = 0
    for i in range(format[0]):
        for j in range(format[1]):
            img_R = img[i, j, 0]
            img_G = img[i, j, 1]
            img_B = img[i, j, 2]
            img_I = img[i, j, 3]
            if ((img_R > 0) and (img_G < 0.3) and (img_B > 0.4) and (img_I > 0.0)):
                new_img[i, j, 3] = 0
                count += 1
            else:
                new_img[i, j, 3] = 1
    if (count > 0):
        proportion = taille/count
    else:
        proportion = taille
    return new_img, proportion

# Check_Prop : check la proportion de pixel blanc et en deduit la presence de la cible
def check_prop(prop):
    ret = ""
    if prop < 10:
        ret = "Cible reperee"
        print('Cible reperee pour n =  '+str(prop))
    else:
        ret = "Pas de cible"
        print('Cible non reperee, n = '+str(prop))
    return ret

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
    first = False
    second = True
    format = np.shape(img)
    for i in range(format[0]):
        for j in range(format[1]):
                if (img[i,j] == 255):
                    bords.append([i,j])
                    first = True
                    break
    for i in range(format[0]):
        for j in range(format[1]):
            if (img[format[0]-i,img[format[1]-j]] == 255):
                bords.append([format[0]-i,img[format[1]-j]])
                second = True
                break  
    print('BORDS : ' + str(bords))
    if(first and second):
        center = ((bords[1][0]-bords[0][0])//2 + bords[0][0],bords[0][1])
    return center                  
                        
                        
                 
        
    def get_pointeur_position(img):
        bords = [(-1,-1),(-1,-1)]
    first = True
    second = True
    format = np.shape(img)
    for i in range(format[0]):
        for j in range(format[1]):
            if(second or first):
                    if (img[i,j] == 255) and first:
                        bords[0] = (i,j)
                        img[i,j] = 0
                        first = False
                        if (img[i,j+1] == 0) and second:
                            bords[1] = (i,j)
                            img[i,j] = 0
                            second = False
                            break
    
    print('BORDS : ' + str(bords))
    center = ((bords[1][1]-bords[0][1])//2 + bords[0][1],bords[0][0])
    return center      