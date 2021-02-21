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
#drawn circles and then going to join these
        rectangle = cv2.boundingRect(ch)
        divide_2d = cv2.Subdiv2D(rectangle)
        divide_2d.insert(points)
        triangles = divide_2d.getTriangleList()
        split_triangle = numpy.array(triangles, dtype=numpy.int32)
        cv2.fillConvexPoly(mask, ch, 255)
        face_image_1 = cv2.bitwise_and(img1, img1, mask=mask)
        face_points2 = numpy.array(points, numpy.int32)
        ch2 = cv2.convexHull(face_points2)
        def extract_index_nparray(nparray):
            index = None
            for num in nparray[0]:
                index = num
                break
            return index
        join_indexes = []
        for edge in triangles:
            first = (edge[0], edge[1])
            second = (edge[2], edge[3])
            third = (edge[4], edge[5])
            index_edge1 = numpy.where((points == first).all(axis=1))
            index_edge1 = extract_index_nparray(index_edge1)
            index_edge2 = numpy.where((points == second).all(axis=1))
            index_edge2 = extract_index_nparray(index_edge2)
            index_edge3 = numpy.where((points == third).all(axis=1))
            index_edge3 = extract_index_nparray(index_edge3)
            if index_edge1 is not None and index_edge2 is not None and index_edge3 is not None:
                triangle = [index_edge1, index_edge2, index_edge3]
                join_indexes.append(triangle)    
        source_mask = numpy.zeros_like(img1_gs)
        new_face = numpy.zeros_like(img2)
        for index in triangles:
            tri_one = points[index[0]]
            tri_two = points[index[1]]
            tri_three = points[index[2]]
            triangle1 = numpy.array([tri_one, tri_two, tri_three], numpy.int32)
            first_rect = cv2.boundingRect(triangle1)
            (x, y, w, h) = first_rect
            cropped_triangle = img1[y: y + h, x: x + w]
            cropped_tr1_mask = numpy.zeros((h, w), numpy.uint8)
            pts = numpy.array([[tri_one[0] - x, tri_one[1] - y],[tri_two[0] - x, tri_two[1] - y], [tri_three[0] - x, tri_three[1] - y]], numpy.int32)
            cv2.fillConvexPoly(cropped_tr1_mask, pts, 255)
            cv2.line(source_mask, tri_one, tri_two, 255)
            cv2.line(source_mask, tri_two, tri_three, 255)
            cv2.line(source_mask, tri_one, tri_three, 255)
cv2.imshow('Test',cv2.resize(source_mask,(640,480)))
#2nd image
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
        cv2.circle(img2, center=(x, y), radius=6, color=(255, 0, 0), thickness=-1)
#example......
cv2.imshow('Face 1',cv2.resize(img1, (640, 480)))
cv2.waitKey(0) 
cv2.imshow('Face 2',cv2.resize(img2, (640, 480)))
#img_final = some processed swapped image
# cv2.imshow("Desired Image",cv2.resize(img_final,(640,480))) image displayed like the inputted one but processed.
#afterwards The End
cv2.waitKey(0) 
cv2.destroyAllWindows 