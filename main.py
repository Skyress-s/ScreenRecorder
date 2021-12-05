import datetime

from PIL import ImageGrab #pip install Pillow
import numpy as np # gets imported with cv2
import cv2
from win32api import GetSystemMetrics # pip install pywin32
import pyautogui


from desktopmagic.screengrab_win32 import (
getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
getRectAsImage, getDisplaysAsImages)


interval = 500

# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
print(time_stamp)

monitor = 1 # 0 is the first monitor, 1 is the second monitor


rects = getDisplayRects()
print(rects)

print(rects[1][1])


fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
# here we have to get the correct screen size or else we get an error, we there det the delta og the display rect
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (rects[monitor][2] - rects[monitor][0], rects[monitor][3] - rects[monitor][1]))
while True:
    # grabs the image
    img = ImageGrab.grab(bbox=(rects[monitor][0], rects[monitor][1], rects[monitor][2], rects[monitor][3]))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)




    #wecam part

    #_, frame = web_cam.read()
    #frameheight, frameWidth, _ = frame.shape
    # # # # cv2.imshow('web cam', frame)
    #img_final[0:frameheight, 0:frameWidth, :] = frame [0: frameheight, 0: frameWidth, : ]

    #webcam part end
    cv2.imshow('secret name', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(interval) == ord('q'):
        break