import cv2
import os
import numpy as np
from matplotlib import pyplot as plt 
import math


def op_log(img,c):
    if img is not None:

        col=['r','g','b']
        for i in range(len(img[0][0])):
            h=cv2.calcHist([img], [i], None, [256], [0, 256])

        plt.show()
        
        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)

        #aplicamos el Histogram equalization en los 3 canales
        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                #aplicamos la formula de raiz
                for k in range(img.shape[1]):
                    vtmp=math.log10(1+img[j][k][i])*c
                    if vtmp>255:
                        vtmp=255
                    out[j][k][i]=vtmp

        for i in range(len(out[0][0])):
            h=cv2.calcHist([out], [i], None, [256], [0, 256])

        return(out,True)

    else:
        return(None,False)
        
def op_sqrt(img,c):
    if img is not None:

        col=['r','g','b']
        for i in range(len(img[0][0])):
            h=cv2.calcHist([img], [i], None, [256], [0, 256])


        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)

        #aplicamos el Histogram equalization en los 3 canales
        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                #aplicamos la formula de raiz
                for k in range(img.shape[1]):
                    vtmp=math.sqrt(1+img[j][k][i])*c
                    if vtmp>255:
                        vtmp=255
                    out[j][k][i]=vtmp

        for i in range(len(out[0][0])):
            h=cv2.calcHist([out], [i], None, [256], [0, 256])


        return(out,True)
    else:
        return(None,False)
        


def run(folder,cc):
    #Procesamos todos los elementos de la carpeta indicada
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        out,ok=op_log(img,cc)
        if ok:
            cv2.imwrite('./outlog/out'+str(cc)+'_'+filename,out)
    final_frame = cv2.hconcat((img, out))
    cv2.imshow('Logaritmo',final_frame)
    cv2.waitKey(1) 

def run_sqrt(folder,cc):
    #Procesamos todos los elementos de la carpeta indicada
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        out,ok=op_log(img,cc)
        if ok:
            cv2.imwrite('./outsqrt/out'+str(cc)+'_'+filename,out)
    final_frame = cv2.hconcat((img, out))
    cv2.imshow('sqrt',final_frame)
    cv2.waitKey(1) 

#Log 
val=5
for i in range(30):
    print("actual "+ str(val))
    run('./input3',val)
    val=val+5


cv2.waitKey(0)
val=5
for i in range(30):
    print("actual "+ str(val))
    run_sqrt('./input3',val)
    val=val+5

#Decidir si lo de abajo es correcto
#en las carpetas se encuentran las imagenes outlog y outsqrt
#Segun yo si xd
# run('./input3',55)#<- mejor valor 
# run('./input3',90)#<- mejor valor

