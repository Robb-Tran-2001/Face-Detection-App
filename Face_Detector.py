import cv2
from random import randrange

#Create classifier from trained data
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Choose example image 
img = cv2.imread('TS.jpg')

#Convert source image (img), 2nd parameter is conversion method (BGR to grayscale)
gs_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect faces, returned as list of rectangles of where the face is
#for the face coords, it is a tuple of size 4:
# x-axis start point, y-axis start point, width, and height
face_coords = classifier.detectMultiScale(gs_img) 

#draw each rectangle with start point, endpoint, color of drawn rectangle, thickness
for(x, y, w, h) in face_coords:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)

#Show image. Wait until any key is pressed to close window
cv2.imshow('Showing Imported Face', img)
cv2.waitKey()

print("Code completed") 