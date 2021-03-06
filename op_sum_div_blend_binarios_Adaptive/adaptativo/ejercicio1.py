import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = min(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

def adaptativo(img,w_size,cf):
    if img is not None:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)
        matriz_umbral=np.zeros(shape=img.shape,dtype=np.uint8)
        submatrix=[]
        parametro=int(w_size/2)
        valores=[0,0,0,0]
        tam=[0,0]
        suma=0

        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                #obtenemos las coordenadas para generar la submatriz
                if i-parametro>=0:
                    valores[0]=i-parametro
                else:
                    valores[0]=0
                if i+parametro<img.shape[0]:
                    valores[1]=i+parametro+1
                else:
                    valores[1]=img.shape[0]
                if j-parametro>=0:
                    valores[2]=j-parametro
                else:
                    valores[2]=0
                if j+parametro<img.shape[1]:
                    valores[3]=j+parametro+1
                else:
                    valores[3]=img.shape[1]
                #generamos la submatriz
                submatrix=np.zeros(shape=[valores[1]-valores[0]-1,valores[3]-valores[2]-1])
                submatrix=img[valores[0]:valores[1]:1,valores[2]:valores[3]:1].copy()
                #sacamos el promedio
                suma=int(np.sum(submatrix)/(submatrix.shape[0]*submatrix.shape[1]))
                suma=suma-cf #restamos con el valor statico
                #aplicamos thresholding
                if img[i][j]>=suma:
                    out[i][j]=255
                else:
                    out[i][j]=0
        
        show_img=hconcat_resize_min([img,out]) 
        cv2.imshow('Adaptivo',show_img)
        cv2.waitKey()
        return(out)
    else:
        return(None)

def run_exp(file1):
    img = cv2.imread(file1)
    out=adaptativo(img,7,1)#segundo parametro debe ser impar mayor que 1
    if out is not None:
        cv2.imwrite('./out/out_paper6_reduced.jpg',out)

run_exp('./input/paper6_reduced.jpg')   