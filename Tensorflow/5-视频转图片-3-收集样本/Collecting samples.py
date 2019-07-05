#视频分解图片
# 1 load    2 info  3 parse   4 imshow  imwrite

import cv2
import time

def read_video():
    i=1300;  
    cap = cv2.VideoCapture(0) # 获取一个视频打开cap    1  file name
    isOpened = cap.isOpened  #  判断是否打开 
    print(isOpened)
    fps = cap.get(cv2.CAP_PROP_FPS)   #获得视频帧率
    width = int (cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 获取宽
    height = int (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 获取高
    print(fps,width,height)

    width = int (64)  # 获取宽
    height = int (128)   # 获取高
    while(isOpened):
        
        flag, frame = cap.read()  
        #cv2.imshow("video", frame)
        if(i>2300):
            print('录制完毕')
            break;
        fileName = 'image'+str(i)+'.jpg'
        print(fileName)
        if (flag==True):
           frame1 = cv2.resize(frame,(width,height))
           cv2.imwrite(fileName,frame1,[cv2.IMWRITE_JPEG_QUALITY,100])
           time.sleep(0.04)  #大概到
           i=i+1
        else:
           break;
    print('end')
    return 

    
read_video()
#cap.release()
cv2.destroyAllWindows()