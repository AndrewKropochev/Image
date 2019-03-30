import math
import numpy as np
import cv2

#start
img = cv2.imread("DR5_wt_r2.tif")

new = np.zeros((1038,1392,3), np.uint8)

#functhion
def summ (i,j):
    sum = (img [i,j][0] + img [i,j][1] + img [i,j][2])/3
    return sum

def arre (i,j):
    pix = summ (i,j)
    index = 0
    
    try:
        index += math.fabs(pix - summ (i-2,j-2))
        index += math.fabs(pix - summ (i-2,j-1))
        index += math.fabs(pix - summ (i-2,j))
        index += math.fabs(pix - summ (i-2,j+1))
        index += math.fabs(pix - summ (i-2,j+2))
        
        
        index += math.fabs(pix - summ (i-1,j-2))
        index += math.fabs(pix - summ (i-1,j-1))
        index += math.fabs(pix - summ (i-1,j))
        index += math.fabs(pix - summ (i-1,j+1))
        index += math.fabs(pix - summ (i-1,j+2))
        
        index += math.fabs(pix - summ (i,j-2))  
        index += math.fabs(pix - summ (i,j-1))   
        index += math.fabs(pix - summ (i,j+1))
        index += math.fabs(pix - summ (i,j+2))
        
        index += math.fabs(pix - summ (i+1,j-2))
        index += math.fabs(pix - summ (i+1,j-1))
        index += math.fabs(pix - summ (i+1,j))
        index += math.fabs(pix - summ (i+1,j+1))
        index += math.fabs(pix - summ (i+1,j+2))
        
        index += math.fabs(pix - summ (i+2,j-2))
        index += math.fabs(pix - summ (i+2,j-1))
        index += math.fabs(pix - summ (i+2,j))
        index += math.fabs(pix - summ (i+2,j+1))
        index += math.fabs(pix - summ (i+2,j+2))
    except: index = 0
    return index
    
#go
print(img.shape)
#img [:,:, 1] = 0
#img [:,:, 0] = 0


i = 0
while i < (1038/1):
    j = 0
    while j < (1392/1):
        new [i,j] = [0,0,arre(i,j)]
        j += 1
    i += 1
    
maks = 0
i = 0
while i < (1038/8):
    j = 0
    while j < (1392/8):
        if maks < new [i,j][2]:
            maks = new [i,j][2]
        j += 1
    i += 1
    
    
    

px = new [100,100]
px0 = img [100,100][0]
print(px)
print(px0)
print(maks)


cv2.imwrite("gradient.jpg", img)
cv2.imwrite("new.jpg", new)