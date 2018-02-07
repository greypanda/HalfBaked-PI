# pip3 install picamera
# python3 bake.py

import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
camera.start_preview()
camera.annotate_text = 'Press return to take a picture!'
result = input('hit a key')
# Take a picture including the annotation
camera.capture('foo.jpg')

