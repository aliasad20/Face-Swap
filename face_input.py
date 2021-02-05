import cv2
import dlib
src1 = input("Enter first image location") #for colelcting the source path of image with the full image name and extension written.
src2 = input("Enter second image location") #for colelcting the source path of image with the full image name and extension written.
img1 = cv2.imread(''+src1) #example to be entered in src: "C:\Users\user\Picturesa.jpg" or " /home/user/Pictures/a.jpg." 
img2 = cv2.imread(''+src2) #example to be entered in src: "C:\Users\user\Picturesa.jpg" or " /home/user/Pictures/a.jpg." 
#.........................Input Section Over....................#
cv2.imshow('Me',cv2.resize(img1, (640, 480))) #for showing and resizing the first image.  
cv2.waitKey(0) # waits for any key to be pressed.
cv2.destroyAllWindows #closes the window in which image is displayed
#...................First Image Displayed and Closed............#
cv2.imshow('Me',cv2.resize(img2, (640, 480))) #for showing and resizing the second image. 
cv2.waitKey(0) # waits for any key to be pressed.
cv2.destroyAllWindows #closes the window in which image is displayed
#..................Second Image Displayed and closed
#now some image processing will be done on these images which will be diaplayed in a third image oject.
#After some processing and swapping done image will be displayed
#   .
#   . //Statements to be written.
#   .  
#example......
#img_final = some processed swapped image
# cv2.imshow("Desired Image",cv2.resize(img_final,(640,480))) image displayed like the inputted one but processed.
#afterwards The End
cv2.waitKey(0) 
cv2.destroyAllWindows 