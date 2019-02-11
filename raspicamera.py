from picamera import PiCamera
import time
import os

camera = PiCamera()

time_stamp = str(int(time.time()))

print(time_stamp)

#camera.rotation = 180
camera.capture('/home/pi/YOLO_images/'+time_stamp+'.jpg')
time.sleep(5)

print("alkaa..")
os.system ("cd /home/pi/darknet")
os.system("./darknet detect cfg/yolov2.cfg ./yolo.weights /home/pi/YOLO_images/"+time_stamp+".jpg")
os.system("mv predictions.png results/"+time_stamp+".png")
time.sleep(0)
print("loppuu..")
