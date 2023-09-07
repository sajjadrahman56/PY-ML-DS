# import cv2 as cv
# import numpy as np
#
# img1 = np.zeros((250,500,3),np.uint8)
# img1 = cv.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
# img2 = cv.imread("F:/amra/sajjad.jpg")
#
# bitAnd = cv.bitwise_and()
#
# cv.imshow("img1",img1)
# cv.imshow("img2",img2)
#
# cv.waitKey(0)
# cv.destroyAllWindows()
# #  #      OpenCV Bitwise AND, OR, XOR, and NOT
# import the necessary packages
import numpy as np
import cv2
# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# draw a circle
circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)


#
# # bitwise_and => return if both image has same pixel " use bitwise_and
#   on the other hand , or count all pixel . This application term works is general concept of bitwise operator
#
bitwiseAnd = cv2.bitwise_or(rectangle, circle)
cv2.imshow("AND", bitwiseAnd)

cv2.waitKey(0)
cv2.destroyAllWindows()