#视频分解图片
# 1 load    2 info  3 parse   4 imshow  imwrite

import cv2
import time

i=0;     #  所有视频的名字的变量
numberofvedio = 21  # 所有视频的个数

def read_video(jj):
    global i
    global numberofvedio
    vediename = str(jj)+'.mp4'
    cap = cv2.VideoCapture(vediename) # 获取一个视频打开cap    1  file name
    isOpened = cap.isOpened  #  判断是否打开 
    print(isOpened)
    fps = cap.get(cv2.CAP_PROP_FPS)   #获得视频帧率
    width = int (cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽
    height = int (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 获取高
    print(fps,width,height)
    while(isOpened):
        (flag,frame) = cap.read() #读取每一张 flag 是否读取成功  frame 图片内容
        if(frame is None):
            print('播放完毕')
            break;
        fileName = 'image'+str(i)+'.jpg'
        print(fileName)
        if (flag==True):
           cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])
           time.sleep(0.04)  #大概到
           i=i+1
        else:
           break;
    print('vedio'+str(jj)+'end')
    return 

def main():
    global i
    global numberofvedio
    for num in range(1,numberofvedio):
        read_video(num)
    return 

main()