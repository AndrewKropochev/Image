import math
import numpy as np
import cv2
import sys
        
def summ (i,j,img):
    res_sum = (img [i,j][0] + img [i,j][1] + img [i,j][2])/3
    return res_sum

def arre (i,j,img,a,b):
    pix = summ (i,j,img)
    index = 0
    
    try:
        ia = -a
        while ia <= a:
            jb = -b
            while jb <= b:
                index += math.fabs(pix - summ (i+ia,j+jb,img))
                jb +=1
            ia +=1
            
    except: index = 0
    return index
    

def main (file,a,b):
    img = cv2.imread(file)
    
    x = img.shape[0]
    y = img.shape[1]
    
    new = np.zeros((x,y,3), np.uint8)
    i = 0
    while i < x:
        j = 0
        while j < y:
            new [i,j] = [0,0,arre(i,j,img,a,b)]
            percent = i*100/x 
            timestr = '\rprogress check - %i%%\t' %(percent)
            sys.stdout.write(timestr)
            sys.stdout.flush()
            j += 1
        i += 1
    
    return new
    
file = "DR5_wt_r2.tif" 
cv2.imwrite("new.jpg", main(file,2,2))

