import cv2

img_file = ''

classifier_file = 'car_detector.xml'

#create opencv image
img = cv2.imread(img_file)

#create classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#convert to grayscale(from black and white)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#display the image with the faces spotted
cv2.imshow('slever programmer car detertor', black_n_white)

#detect cars of any size
cars = car_tracker.detectMultiScale(black_n_white)

for (x,y, w, h) in cars:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0,255),2)
    #             image, x,y, width, height, color, thickness


#draw rectangles around the cars
car1 = cars[0]
(x,y,w,h) =  car1  #unpacking car1
cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0,255),2)


cv2.imshow('clever  car detector', img)
# dont autoclose (listen for key press)
cv2.waitKey()

print("code ocompleted")
