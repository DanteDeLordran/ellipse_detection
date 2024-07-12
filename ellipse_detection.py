import cv2
import numpy as np

img = cv2.imread('circles6.jpg', 0)
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 50, param1=80, param2=20, minRadius=3, maxRadius=25)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('Circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

t2 = cv2.imread('circles6.jpg')
thresh = cv2.cvtColor(t2, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 101, 0)
count, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)
for i in range(1, count):
    t2 = cv2.circle(t2, (int(centroids[i, 0]), int(centroids[i, 1])), 5, (0, 255, 0, 0), 5)

cv2.imshow('Centers', t2)
cv2.waitKey()
