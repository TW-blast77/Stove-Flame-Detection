import cv2
import os
import glob

video_number = 1
video_dir = glob.glob('./env01/Video/*.mp4', recursive=True)

for video_path in video_dir:
    cap = cv2.VideoCapture(video_path)
    isOpened = cap.isOpened()  
    print(isOpened)
    
    n_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  
    print('總幀數：', n_frame)
    fps = cap.get(cv2.CAP_PROP_FPS)  
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
    print('幀數、寬度、高度分別為：', fps, width, height)

    frame_index = 0 
    frame_frequency = int(fps)  
    while isOpened:
        if frame_index >= n_frame:
            break
        else:
            frame_index += 1
        
        flag, frame = cap.read()  
        if not flag:
            break  

        if frame_index % frame_frequency == 0:
            fileName = '\\video[' + str(video_number) + ']_' + 'image' + str(frame_index) + ' .jpg'
            outPutDirName = 'E:\\Yolov7\\env01\\Output_Picture'
            if not os.path.exists(outPutDirName):
                os.makedirs(outPutDirName)
            print(fileName)
            cv2.imwrite(outPutDirName + fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])  
        
    cap.release()  
    video_number += 1
    print('分割完成 !')
