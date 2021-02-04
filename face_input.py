import cv2

src1 = input("Enter first image location") #for colelcting the source path of image with the full image name and extension written.
src2 = input("Enter second image location") #for colelcting the source path of image with the full image name and extension written.
img1 = cv2.imread(''+src1) #example to be entered in src: "C:\Users\user\Picturesa.jpg" or " /home/user/Pictures/a.jpg." 
img2 = cv2.imread(''+src2) #example to be entered in src: "C:\Users\user\Picturesa.jpg" or " /home/user/Pictures/a.jpg." 
cv2.imshow('Me',cv2.resize(img1, (640, 480))) #for showing and resizing the image being displayed
cv2.waitKey(0) # waits for any key to be pressed.
cv2.destroyAllWindows #closes the window in which image is displayed