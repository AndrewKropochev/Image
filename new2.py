
import numpy as np
import cv2


image = cv2.imread("new.jpg")

kernel0 = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(image,-1,kernel0)


gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)


ret,thresh = cv2.threshold(gray, 18, 220, cv2.THRESH_BINARY)
cv2.imwrite("thresh.jpg", thresh)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))   
newthresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#new2thresh = cv2.morphologyEx(newthresh, cv2.MORPH_CLOSE, kernel)
new3thresh = cv2.morphologyEx(newthresh, cv2.MORPH_OPEN, kernel2)
cv2.imwrite("newthresh.jpg", new3thresh)

