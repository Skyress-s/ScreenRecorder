import datetime

from PIL import ImageGrab #pip install Pillow
import numpy as np # gets imported with cv2
import cv2
from win32api import GetSystemMetrics # pip install pywin32

interval = 60

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
print(time_stamp)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

#webcam part
web_cam = cv2.VideoCapture(0) # 0 gets the first camera
#webcampart end

while True:
    img = ImageGrab.grab(bbox=(0,0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

    #wecam part

    _, frame = web_cam.read()
    frameheight, frameWidth, _ = frame.shape
    # cv2.imshow('web cam', frame)
    img_final[0:frameheight, 0:frameWidth, :] = frame [0: frameheight, 0: frameWidth, : ]

    #webcam part end
    cv2.imshow('secret name', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(interval) == ord('q'):
        break