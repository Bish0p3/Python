from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('input.jpg')
imgcopy = cv2.imread('input.jpg')
cv2.resize(img, (300,300))

p1 = ()
p2 = ()
p3 = ()
p4 = ()
points = [p1,p2,p3,p4]
count = 0

def mouse_drawing(event, x, y, flags, params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(imgcopy, (x, y), 3, (0, 0, 255), -1)
            cv2.imshow("Input",imgcopy)
            points[count] = (x, y)
            print('Point ')
            print(count+1)
            print(x,y)
    if event == cv2.EVENT_LBUTTONUP:
        count = count + 1
    if count == 4:
        pts1 = np.float32 ([points[0],points[1],points[2],points[3]])
        pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
        
        M = cv2.getPerspectiveTransform(pts1,pts2)
        dst = cv2.warpPerspective(img,M,(300,300))

        cv2.imwrite('Output.jpg',dst) 
        cv2.destroyAllWindows()
        cv2.imshow("Output", dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
cv2.namedWindow("Input")
cv2.setMouseCallback("Input", mouse_drawing)
cv2.imshow("Input", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

        







