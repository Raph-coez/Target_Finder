# Imports
import matplotlib.pyplot as mplot
import numpy as np
from algos import *

# Choix de l'image a tester
img = mplot.imread('./images/image_1.png')
print(np.shape(img))

# Choix des algos
new_img_1 = TOR_blue(img)
new_img_2 = TOR_cyan(img)
new_img_3 = TOR_magenta(img)

# Affichage du test
    # Affichage algo_1
mplot.subplot(321)
mplot.imshow(img)
mplot.axis('off')
mplot.title('Image a traiter')
mplot.subplot(322)
mplot.imshow(TOR_blue(img))
mplot.axis('off')
mplot.title('Image traitee via TOR_blue')

    # Affichage algo_2
mplot.subplot(323)
mplot.imshow(img)
mplot.axis('off')
mplot.title('Image a traiter')
mplot.subplot(324)
mplot.imshow(TOR_cyan(img))
mplot.axis('off')
mplot.title('Image traitee via TOR_cyan')

    # Affichage algo_3
mplot.subplot(325)
mplot.imshow(img)
mplot.axis('off')
mplot.title('Image a traiter')
mplot.subplot(326)
mplot.imshow(TOR_magenta(img))
mplot.axis('off')
mplot.title('Image traitee via TOR_magenta')
mplot.show()
