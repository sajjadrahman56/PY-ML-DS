import numpy as np
import cv2 as cv
def nothing(x):
    print(x)
# create a black image window
img = np.zeros((300,500,3),np.uint8)
cv.namedWindow("image");

switch = '0 : OFF\n 1 : ON'

cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar(switch,'image',0,1,nothing)

while(1):
    cv.imshow('image',img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    b = cv.getTrackbarPos('B','image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv.destroyAllWindows()
