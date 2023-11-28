import cv2
import time
def takepicture():
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`

    while(True): #display the captured image
        cv2.imwrite('static/file.jpg',frame)
        break
    cap.release()
takepicture()