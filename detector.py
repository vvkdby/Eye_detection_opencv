import numpy as np
import cv2
import simplejson as json

#these are the downloaded classifier files that OpenCV provides us
#OpenCV's cascade classifier class
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_detector = cv2.CascadeClassifier('haarcascade_eye.xml')

#input the file name (assumes it is in the same folder)
filename = raw_input()

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#performing face detection
faces = face_detector.detectMultiScale(gray, 1.3, 5)

for (x,y,w,h) in faces:
    #visualization of the face
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    #performing eye detection
    eyes = eye_detector.detectMultiScale(roi_gray)
    #printing out values in JSON format
    for i in range(len(eyes)):
        avg_x = (eyes[i][0] + eyes[i][2])/2
        avg_y = (eyes[i][1] + eyes[i][3])/2
        print json.dumps({"x":avg_x,"y":avg_y},sort_keys= True)
    #visualization of eyes
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#visualization handles
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()