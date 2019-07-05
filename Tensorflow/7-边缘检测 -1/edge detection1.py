# sobel  算子  边缘检测
import cv2
import numpy as np
import random 
import math

img = cv2.imread('image0.jpg',1) #灰度图片打开
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
cv2.imshow('src',img)
#sobel边缘检测     1 算子模版  2  图片卷积  3 阈值判决

#  竖直方向算子              水平方向算子
#【 1  2   1               【1  0  -1
#   0  0  0                2  0  -2
#  -1 -2 -1 】            1  0  -1】

#【1,2,3,4】图像信息  【a,b,c,d】卷积模版    a*1+b*2+c*3+d*4 = dat  卷积值
#a 水平方向卷积值 b 竖直方向卷积值 
#sqrt(a*a+b*b)  = f  >  th    阈值判断

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #1  
dat = np.zeros((height,width,1),np.uint8)
for i in range(0,height-2):
    for j in range(0,width-2):
        gy = gray[i,j]*1+gray[i,j+1]*2+gray[i,j+2]*1 -  gray[i+2,j]*1 - gray[i+2,j+1]*2 - gray[i+2,j+2]*1
        gx = gray[i,j]*1+gray[i+1,j]*2+gray[i+2,j]*1 -  gray[i,j+2]*1 - gray[i+1,j+2]*2 - gray[i+2,j+2]*1
        grad = math.sqrt(gx*gx+gy*gy)
        if grad > 50:
            dat[i,j] =255
        else:
            dat[i,j]=0
cv2.imshow('dat',dat)
cv2.waitKey(0)

#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #1
#imgG = cv2.Canny(img,50,50) #  1 data  2  th  
#cv2.imshow('dat',dat)
#cv2.waitKey(0)
