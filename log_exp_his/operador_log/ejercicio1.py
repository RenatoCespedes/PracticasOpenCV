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
        #nueva imagen
        out=np.zeros(shape=img.shape,dtype=np.uint8)
        #aplicamos el Histogram equalization en los 3 canales
        for i in range(len(img[0][0])):
            for j in range(img.shape[0]):
                for k in range(img.shape[1]):
                    vtmp=math.log10(1+img[j][k][i])*c
                    if vtmp>255:
                        vtmp=255
                    out[j][k][i]=vtmp

        return(out,True)
    else:
        return(None,False)
        


def run(folder,cc):
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        out,ok=op_log(img,cc)
        if ok:
            cv2.imwrite('./out/out'+str(cc)+'_'+filename,out)
    final_frame = cv2.hconcat((img, out))
    cv2.imshow('Logaritmo',final_frame)
    cv2.waitKey(1) 
#Imagen 1
val=0
for i in range(20):
    print('actual'+str(val))
    run('./input1_11',val)
    val=val + 10
cv2.waitKey(0)
#Imagen 2    
val=0
for i in range(20):
    print('actual'+str(val))
    run('./input1_1',val)
    val=val + 10
cv2.waitKey(0)
#Imagen 3 Ejercicio 2
val=0
for i in range(20):
    print('actual'+str(val))
    run('./input2',val)
    val=val + 10
# run('./input1_11',50)
# run('./input1_1',50)
# run('./input1_11',70)
# run('./input1_1',70)
# run('./input1_11',90)
# run('./input1_1',90)
# # run('./input1_11',100) #<- segun analisis visual el mejor valor
# # run('./input1_1',100)
# run('./input1_11',120)
# run('./input1_1',120)
