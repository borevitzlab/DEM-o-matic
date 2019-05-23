import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import sys
in_file = sys.argv[1]
out_file = sys.argv[2]

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

def exp_transform_image(init_file, final_file):
    """
    Applies a natural exponent to all pixels in image. 
    """
    # get file
    img = mpimg.imread(init_file)

    # avoid division by 0
    img = img * 100
    img = img+1
    img = img / 100

    # raise all values to n to undo log
    img = np.exp(img)
    img = (img-np.amin(img))/(np.amax(img)-np.amin(img))
    #print(img)
    plt.imsave(final_file, img, cmap='Greys_r')

exp_transform_image(in_file, out_file)
