
# 1 引入opencv 2 API 3 stop
import cv2 
# 1文件读取  2封装格式解析  3 数据解码  4 数据加载
img = cv2.imread('image0.jpg',1) # read image 1 name 2 0 gray 1 color 
# jpg png  1 文件头  2 文件数据
cv2.imshow('image',img) # 1 name win 2 img data
cv2.waitKey(0)

import cv2
img = cv2.imread('image0.jpg',1)
cv2.imwrite('image1.jpg',img)   # 1 name 2 data

import cv2
img = cv2.imread('image0.jpg',1)
cv2.imwrite('image1.jpg',img,[cv2.IMWRITE_PNG_COMPRESSION,0])   # 0-9 无损 压缩

import cv2
img = cv2.imread('image0.jpg',1)
cv2.imwrite('image1.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,50])   # 0-100 有损压缩