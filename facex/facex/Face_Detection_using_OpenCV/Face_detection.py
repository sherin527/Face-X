import cv2 as cv


face_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv.imread("face.jpg")
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)




cv.imshow('face',img)
cv.waitKey(0)
