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


def dec_to_bin(numero1,numero2):
    bin1=bin(numero1)[2:]
    bin2=bin(numero2)[2:]
    while len(bin1)<len(bin2):
        bin1="0"+bin1
    while len(bin1)>len(bin2):
        bin2="0"+bin2
    return bin1,bin2

def bin_to_dec(t_cadena):
    return int(t_cadena,2)

def op_xor(pixel1,pixel2):
    cadena1,cadena2=dec_to_bin(pixel1,pixel2)
    temp_cadena=""
    #operacion xor
    for i in range(len(cadena1)):
        if cadena1[i]!= cadena2[i]:
            temp_cadena=temp_cadena+"1"
        else:
            temp_cadena=temp_cadena+"0"
    return bin_to_dec(temp_cadena)
def op_binario(imname1,imname2,operacion):
    img=cv2.imread(imname1)
    img2=cv2.imread(imname2)
    if img is not None and img2 is not None:


        out=np.zeros(shape=img2.shape,dtype=np.uint8)
        #aplicamos las operaciones binarias
        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                for k in range(img.shape[1]):
                    out[j][k][i]=op_xor((img2[j][k][i]),(img[j][k][i]))

        show_img=hconcat_resize_min([img,img2,out]) 
        cv2.imshow('Operacion Binaria XOR',out)
        cv2.waitKey()
        return(out)
    else:
        return(None)

operacion="xor"
out=op_binario('./input1/img1.jpeg','./input1/img2.jpeg',operacion)
cv2.imwrite('./output/out_'+str(operacion)+'.jpeg',out)