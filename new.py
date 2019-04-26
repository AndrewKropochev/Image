import math
import numpy as np
import cv2

#functhion
def summ (i,j,img):
    sum = (img [i,j][0] + img [i,j][1] + img [i,j][2])/3
    return sum

def arre (i,j,img):
    pix = summ (i,j,img)
    index = 0
    
    try:
        index += math.fabs(pix - summ (i-2,j-2,img))
        index += math.fabs(pix - summ (i-2,j-1,img))
        index += math.fabs(pix - summ (i-2,j,img))
        index += math.fabs(pix - summ (i-2,j+1,img))
        index += math.fabs(pix - summ (i-2,j+2,img))
        
        
        index += math.fabs(pix - summ (i-1,j-2,img))
        index += math.fabs(pix - summ (i-1,j-1,img))
        index += math.fabs(pix - summ (i-1,j,img))
        index += math.fabs(pix - summ (i-1,j+1,img))
        index += math.fabs(pix - summ (i-1,j+2,img))
        
        index += math.fabs(pix - summ (i,j-2,img))  
        index += math.fabs(pix - summ (i,j-1,img))   
        index += math.fabs(pix - summ (i,j+1,img))
        index += math.fabs(pix - summ (i,j+2,img))
        
        index += math.fabs(pix - summ (i+1,j-2,img))
        index += math.fabs(pix - summ (i+1,j-1,img))
        index += math.fabs(pix - summ (i+1,j,img))
        index += math.fabs(pix - summ (i+1,j+1,img))
        index += math.fabs(pix - summ (i+1,j+2,img))
        
        index += math.fabs(pix - summ (i+2,j-2,img))
        index += math.fabs(pix - summ (i+2,j-1,img))
        index += math.fabs(pix - summ (i+2,j,img))
        index += math.fabs(pix - summ (i+2,j+1,img))
        index += math.fabs(pix - summ (i+2,j+2,img))
    except: index = 0
    return index
    

def main (file):
    img = cv2.imread(file)
    
    x = img.shape[0]
    y = img.shape[1]
    
    new = np.zeros((x,y,3), np.uint8)

    i = 0
    while i < x:
        j = 0
        while j < y:
            new [i,j] = [0,0,arre(i,j,img)]
            j += 1
        i += 1
    
    maks = 0
    i = 0
    while i < (x):
        j = 0
        while j < (y):
            if maks < new [i,j][2]:
                maks = new [i,j][2]
            j += 1
        i += 1
    
    cv2.imwrite("new.jpg", new)
    return maks
