
import numpy as np
import cv2

##reading previously got image
temp_image = cv2.imread("new.jpg")

kernel0 = np.ones((5,5),np.float32)/25
##I don't know what it means because without it work too
dst = cv2.filter2D(temp_image,-1,kernel0)
##1 channel image (shape = 1038, 1392)
gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

ret,thresh = cv2.threshold(gray, 19, 220, cv2.THRESH_BINARY)
cv2.imwrite("thresh.jpg", thresh)
#tresholding
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
maxArea = 0
for c in contours:
    area = cv2.contourArea(c) # площадь
    if maxArea < area:
        contour = c
        maxArea = area
#find contours
img = cv2.imread("DR5_wt_r1.tif") ##original image

#use convex contour
hull = cv2.convexHull(contour)
cv2.drawContours(img, [hull], -1, (0, 0, 255), 6)
#draw red contour to get it late

cv2.imwrite("contour.jpg", img)
root = cv2.imread("DR5_wt_r1.tif")
#read orig image again


cont_pic = cv2.imread("contour.jpg")
#find intensity in red channel
red = cont_pic[:,:,2]
red[red < 250] = 0
red[red != 0] = 1
#res = root*red #older not true

for i in range(len(img)):
    for j in range(len(img[i])):
        if red[i, j] == 0:
            root[i, j, :] = 0
        else:
#            break
        #its earlier realization
            i = 0
            j = j+1
        

cv2.imwrite("res.jpg", root)

