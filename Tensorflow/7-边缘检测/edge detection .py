import cv2
import numpy as np
import random 

img = cv2.imread('image0.jpg',1) #灰度图片打开
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
#canny边缘检测     1 转换gray  2  高斯滤波  3 canny边缘检测

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #1  
imgG = cv2.GaussianBlur(gray,(3,3),0) 
dat = cv2.Canny(imgG,50,50)   #1  data  2th 图片卷积
cv2.imshow('dat',dat)
cv2.waitKey(0)

#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #1
#imgG = cv2.Canny(img,50,50) #  1 data  2  th  
#cv2.imshow('dat',dat)
#cv2.waitKey(0)
