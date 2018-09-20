
# Created by Qinglang Yu and Shreenidhi Jayaram
# EC 463 Mini Project

import cv2
print(cv2.__version__)

cascade_src = 'carss.xml'   #Source file
video_src = 'CommAveVid.avi' #input file

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read() #openup the file and start encrypting
    if (type(img) == type(None)):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) # outline the frame for the detected cars

    cv2.imshow('video', img)
    print ("Found "+str(len(cars))+" car(s)") #priting the num of detected cars
    arr_car=str(len(cars)) #create a list that stores the num of detected vehicles
    num_car= float(arr_car)
    if num_car>=5:
        print ("continued")
    else:
        print ("no car detected") #output when zero car is detected from the video
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
