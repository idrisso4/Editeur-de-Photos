# Author: idrisso4

# Import Libraries
import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt

def lecture_img(file):
    img=mpimg.imread(file)
    return(img)

def r90d(im):
    hauteur, largeur, couleur = im.shape
    imgd = np.zeros((largeur,hauteur,couleur))
    for i in range(hauteur):
        imgd[:,hauteur-i-1]=im[i]
    return(imgd)

def green(img):
    imgvert = np.zeros(img.shape)
    imgvert [ : , : , 1] = img [ : , : , 1]
    return(imgvert)

def negatif(img):
    imginverse = 1-img
    return(imginverse)

def gray(img):
    imggris = (img[ : , : , 0] + img[ : , : , 1] + img[ : , : , 2])/3
    return(imggris)
