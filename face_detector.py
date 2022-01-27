import numpy as np
import cv2

#now laoding some pretrained data on the opencv haarcascade algorithm
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#select an image to work with
img = cv2.imread('ml4.png')
webcam = cv2.VideoCapture(0)
#iterate forever over frame
while True:
    #read the current frame
    successful_frame_read, frame = webcam.read()
    #must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#converting to greyscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

#creates an array for the image so if you have mhultiple images its goimg to detect acording to that array

(x, y, w, h) = face_coordinates[1]
#or you can creata a for loop for it
#draw rectangles around the face
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

print(face_coordinates)


#displaying the image
cv2.imshow('Face Detector', img)

cv2.waitKey()

print("so guys the code is working perdectly fine")
