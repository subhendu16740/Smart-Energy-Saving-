import workingDetect
import faceDe 
import time
import GPIOW
import io
import bluetooth
import RPi.GPIO as GPIO 


import os
import picamera
import cv2
import numpy

def face():
#def isDetected():
    #Create a memory stream so photos doesn't need to be saved in a file
    stream = io.BytesIO()

    #Get the picture (low resolution, so it should be quite fast)
    #Here you can also specify other parameters (e.g.:rotate the image)
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.hflip = True
        camera.capture(stream, format='jpeg')


    #Convert the picture into a numpy array
    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

    #Now creates an OpenCV image
    image = cv2.imdecode(buff, 1)

    #Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('face1.xml')

    #Convert to grayscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    #print("Found faces", str(len(faces)))
    ret = False
        #Draw a rectangle around every found face
    ct = 0
    for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
            ct+=1
    print( ct )
    
    cv2.imwrite('result535.jpg',image)

    #Save the result image
    if ct > 1:
        return 1
    else:
        return 0

       #calling for header file which helps in using GPIOs of PI
LED=21

GPIO.setmode(GPIO.BCM)     #programming the GPIO by BCM pin numbers. (like PIN40 as GPIO21)
# Setup your channel
GPIO.setwarnings(False)
GPIO.setup(LED,GPIO.OUT)  #initialize GPIO21 (LED) as an output Pin
GPIO.output(LED,0)

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
     
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,address = server_socket.accept()
print("Accepted connection from ",address)

def gpioWork(res):
        
        GPIO.output(LED,0)
        channel_is_on = GPIO.input(LED)  # Returns 0 if OFF or 1 if ON
        print("value of channel_is_on ",channel_is_on)
        z= face()
        if not channel_is_on:
            data = res
            print("data ",data)
            if (data == 0 and z == 0):    #if '0' is sent from the Android App, turn OFF the LED
                take_data = client_socket.recv(1024)
                take_data = int(take_data) 
                print("value of take_data ",take_data)
                if (take_data == 0):
                    GPIO.output(LED,1)
                
            
            
            

# execute only if run as a script
def main():

    while True:
        print("hello")
        res = workingDetect.motion()
        print(res)
        GPIOW.gpioWork(res)
       
    client_socket.close()
    server_socket.close()

main()
