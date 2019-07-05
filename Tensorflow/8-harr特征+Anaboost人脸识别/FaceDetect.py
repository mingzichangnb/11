# 1 load xml  2 lod pig  2 gray  4 detect  5 draw
import cv2
import numpy as np

#1 load xml  file name
face_xml = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_xml= cv2.CascadeClassifier('haarcascade_eye.xml')

#2  load jpg
img = cv2.imread('face.jpg')
cv2.imshow('src',img)

#3 hear gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#detect
#灰度  比例缩放  最小5像素
faces = face_xml.detectMultiScale(gray,1.3,5)
print ('face=',len(faces))

#draw
for (x,y,w,h) in faces:
   cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
   roi_face = gray[y:y+h,x:x+w]
   roi_color = img[y:y+h,x:x+w]
   eyes = eye_xml.detectMultiScale(roi_face)
   print('eyse=',len(eyes) )
   for (e_x,e_y,e_w,e_h) in eyes:
        cv2.rectangle(roi_color,(x,y),(x+w,y+h),(255,0,0),2)
        
cv2.imshow('dst',img)
cv2.waitKey(0)
         


