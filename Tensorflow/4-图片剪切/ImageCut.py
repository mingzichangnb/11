
# x 100-200   y  100 -300
import cv2
img = cv2.imread('image0.jpg',1)
imgInfo  = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1] 
mode = imgInfo[2]

# 放大 缩小 任意比例   非等比例
datHeight = int(height*0.5)
datWidth = int(width*0.5)
dst =img[100:200,100:300]
#cv2.imwrite('image1.jpg',dst,[cv2.IMWRITE_JPEG_QUALITY,100])
cv2.imshow('image',dst)
cv2.waitKey(0)