import picamera
import time
import sys
import tty
import time
import termios

camera = picamera.PiCamera()
camera.resolution = (1280,1024)
camera.framerate = 24
bright = camera.brightness
ts = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
while True:
    camera.start_preview(window = (100,100,640,480))
    camera.annotate_text = 'Return: snap, +,- : brightness (' + str(bright) + '), q: quit'
    result = None
    while result not in ['\n','q']:
        result = sys.stdin.read(1)
        if result == '+':
            if bright < 100:
                bright +=1
              camera.brightness = bright
        if result == '-':
             if bright > 0:
                 bright -= 1
                 camera.brightness = bright
            
        camera.annotate_text = 'Return: snap, +,- : brightness (' + str(bright) + '), q: quit'
            # Take a picture including the annotation
    camera.annotate_text = ''
    timestr = time.strftime("%Y%m%d-%H%M%S")
    camera.capture('STILL-' + timestr + '.jpg')
    if result == 'q':
        termios.tcsetattr(sys.stdin,termios.TCSADRAIN,ts)
        sys.exit()
