import cv2
import dlib
import numpy
import time
#Imege should have face upright or else it won't work
src1 = input("Enter first image location: ") #for colelcting the source path of image with the full image name and extension written.
src2 = input("Enter second image location: ") #for colelcting the source path of image with the full image name and extension written.
img1 = cv2.imread(''+src1) #example to be entered in src: "C:\Users\user\Picturesa.jpg" or " /home/user/Pictures/a.jpg." 
img1_gs = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)  
img2 = cv2.imread(''+src2) #example to be entered in src: "C:\Users\user\Picturesa.jpg" or " /home/user/Pictures/a.jpg."
img2_gs = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
mask = numpy.zeros_like(img1_gs)
#.........................Input Section Over....................#
cv2.imshow('Face 1',cv2.resize(img1, (640, 480))) #for showing and resizing the first image.
cv2.waitKey(0) # waits for any key to be pressed.
cv2.destroyAllWindows #closes the window in which image is displayed
#...................First Image Displayed and Closed............#
cv2.imshow('Face 2',cv2.resize(img2, (640, 480))) #for showing and resizing the second image. 
cv2.waitKey(0) # waits for any key to be pressed.
cv2.destroyAllWindows #closes the window in which image is displayed
#..................Second Image Displayed and closed
#now some image processing will be done on these images which will be diaplayed in a third image oject.
#After some processing and swapping done image will be displayed
ld = dlib.get_frontal_face_detector() #landmark detection
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
im1 = ld(img1_gs)
for face in im1:
    landmarks = predict(img1_gs, face)
    points =[] #empty tupple
    for n in range(0,68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        points.append((x, y)) 
        fp = numpy.array(points, numpy.int32)
        ch = cv2.convexHull(fp)
        cv2.circle(img1, center=(x, y), radius=6, color=(0, 255, 0), thickness=-1)
#2nd image
ld = dlib.get_frontal_face_detector() #landmark detection
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
im2=ld(img2_gs)
for face in im2:
    landmarks = predict(img2_gs, face)
    points =[] #empty tupple
    for n in range(0,68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        points.append((x, y)) 
        fp = numpy.array(points, numpy.int32)
        ch = cv2.convexHull(fp)
        cv2.circle(img1, center=(x, y), radius=6, color=(0, 255, 0), thickness=-1)
#example......
cv2.imshow('Face 1',cv2.resize(img1, (640, 480)))
cv2.waitKey(0) 
cv2.imshow('Face 2',cv2.resize(img2, (640, 480)))
#img_final = some processed swapped image
# cv2.imshow("Desired Image",cv2.resize(img_final,(640,480))) image displayed like the inputted one but processed.
#afterwards The End
cv2.waitKey(0) 
cv2.destroyAllWindows 