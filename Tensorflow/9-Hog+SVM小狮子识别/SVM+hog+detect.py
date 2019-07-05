# 1 样本 2 训练 3 test 预测

#样本
#1 正样本pos  2 负样本neg


#1  参数设置  cell block  win   2 创建hog   3 获取svm参数   4 计算hog    5  label  6 train  7 pred  8  draw

import cv2
import numpy as np
import matplotlib.pyplot as plt


# 1  参数设置
PosNum = 820    #正样本个数
NegNum = 1931   #负样本个数
winSize = (64,128)  #窗体大小  图片像素   样本大小
blockSize = (16,16)   #每个块大小  1win = 105 block
blockStride = (8,8)   #           1block = 4 cell
cellSize = (8,8)
nBin = 9            #            1 cell  =  9 bin


#2 创建hog
#hog creat hog  1 win  2 block（大小  步长）  3 blockStride  4 cell大小 5 bin个数
hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nBin)

#3 创建SVM
svm = cv2.ml.SVM_create()

#4 computer hog   计算hog
featureNum = int(((128-16)/8+1)*((64-16)/8+1)*4*9)  #3780    特征维度
featureArray = np.zeros(((PosNum+NegNum),featureNum),np.float32)   #特征数组
labelArray = np.zeros(( (PosNum+NegNum) ,1 ) ,np.int32)            #定义标签

for i in range(0,PosNum):
    fileName = 'pos\\image'+str(i+1)+'.jpg'  #文件名获取
    img = cv2.imread(fileName)
    hist = hog.compute(img,(8,8)) #3780  #文件数据加载到hist
    for j in range(0,featureNum):
        featureArray[i,j]= hist[j]        #放置标签到 featureArray
    labelArray[i,0] = 1
    
for i in range(0,NegNum):
    fileName = 'neg\\image'+str(i+1)+'.jpg'
    img = cv2.imread(fileName)
    hist = hog.compute(img,(8,8)) #3780
    for j in range(0,featureNum):
        featureArray[i+PosNum,j]= hist[j]
    labelArray[i+PosNum,0] = -1

svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

6#train
ret = svm.train(featureArray,cv2.ml.ROW_SAMPLE,labelArray)

7#检测  
alpha = np.zeros(1,np.float32)    # 1行1列
rho = svm.getDecisionFunction(0,alpha)  
print(rho)
print(alpha)
alphaArray = np.zeros((1,1),np.float32)
supportVArray = np.zeros((1,featureNum),np.float32)
resultArray = np.zeros((1,featureNum),np.float32)
alphaArray[0,0] = alpha
resultArray = -1 * alphaArray*supportVArray

#detect
mydetect= np.zeros(3781,np.float32)
for i in range(0,3780):
    mydetect[i]= resultArray[0,i]
mydetect[3780] = rho[0]      #阈值判决 rho--->SVM----》svm.train
    
#构建 hog
myHog = cv2.HOGDescriptor()          #本程序得核心  创建myHog ---》 mydetect---》array---》resultArray & rho
myHog.setSVMDetector(mydetect) #把mydetect属性传递进去

imageSrc = cv2.imread('test3.jpg',1) 
objs = myHog.detectMultiScale(imageSrc,0,(8,8),(32,32),1.05,2)
        #xy   wh  三维
x= int(objs[0][0][0])
y= int(objs[0][0][1])
w= int(objs[0][0][2])
h= int(objs[0][0][3])

#绘制展示
cv2.rectangle(imageSrc,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('opt', imageSrc)
cv2.waitKey(0)
#video_capture.release()
#cv2.destroyAllWindows()



