from scipy.spatial import distance as dist
import numpy as np 
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.resize(image, (0, 0), fx=0.85, fy=0.85)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
thresh = cv2.threshold(blur_image, 200, 255, cv2.THRESH_BINARY_INV)[1]

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c1 in cnts:
	M = cv2.moments(c1)
	cX1 = int(M["m10"] / M["m00"])
	cY1 = int(M["m01"] / M["m00"])
	for c2 in cnts:
		M = cv2.moments(c2)
		cX2 = int(M["m10"] / M["m00"])
		cY2 = int(M["m01"] / M["m00"])
		D = dist.euclidean((cX1, cY1), (cX2, cY2))

		if D<80 and D!=0:
			image = cv2.line(image, (cX2, cY2), (cX1, cY1), (0, 0, 255), 2)
			cv2.drawContours(image, [c2, c1], -1, (0, 0, 255), 2)

		elif D>80 and D<200:
			image = cv2.line(image, (cX2, cY2), (cX1, cY1), (0, 255, 0), 2)

		else:
			continue


cv2.imshow("output", image)
cv2.waitKey(0)
