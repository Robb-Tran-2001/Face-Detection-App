import cv2
from random import randrange

#Create classifier from trained data
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#capture video from webcame
webcam = cv2.VideoCapture(0) #use 0 for webcam, file path name for videos

while True:
    success_read, frame = webcam.read() #boolean if read successfully an the actual frame
    gs_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coords = classifier.detectMultiScale(gs_img)
    for(x, y, w, h) in face_coords:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)
    cv2.imshow('Real time detection', frame)
    key = cv2.waitKey(1) 
    #wait for a key for a ms, so 
    #a frame every millisecond, without waitKey frame does not display
    if key == 81 or key == 113:
        break

webcam.release()