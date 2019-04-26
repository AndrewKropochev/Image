# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:37:15 2019

@author: UbogoevaEV
"""


import cv2
import numpy as np


img = cv2.imread('res.jpg', 0)
#img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
size = np.size(img)
skel = np.zeros(img.shape,np.uint8)
 
ret,img = cv2.threshold(img, 15, 220, 0)
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
done = False
#morphological skeleton transformation 
while( not done):
    eroded = cv2.erode(img,element)
    temp = cv2.dilate(eroded,element)
    temp = cv2.subtract(img,temp)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
 
    zeros = size - cv2.countNonZero(img)
    if zeros==size:
        done = True
skel = cv2.dilate(skel, np.ones((2,6),np.uint8), iterations = 1) #to make line some bigger
max_val = 0
#finding most longer line (in diagonal root its not helpful)
for i in range(len(skel)):
    if np.count_nonzero(skel[i]) > max_val:
        max_val = np.count_nonzero(skel[i])
        true_i = i
#writing result image
cv2.imwrite('line.png', skel)