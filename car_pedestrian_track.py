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

# dont autoclose (listen for key press)
cv2.waitKey()

print("code ocompleted")
