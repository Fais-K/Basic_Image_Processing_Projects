import numpy as np 
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


colors = [[33, 160, 107], [107, 22, 130], [185, 144, 59], [38, 155, 211], [1, 60, 193]]
color_names = ['Green', 'Violet', 'Blue', 'Yellow', 'Orange']
# boundaries = [	([11, 44, 27], [112, 226, 179]),
# 				([30, 24, 15], [229, 194, 145]),
# 				([0, 41, 86], [95, 214, 242]),
# 				([27, 57, 133], [121, 157, 224]),
# 				([91, 35, 143], [209, 133, 201])	]
index = 0

for color in colors:
	color = np.uint8([[color]])
	hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
# for (lower, upper) in boundaries:
	lower_limit = hsv_color[0][0][0] - 6, 100, 100
	upper_limit = hsv_color[0][0][0] + 8, 255, 255

	lower = np.array(lower_limit)
	upper = np.array(upper_limit)

	mask = cv2.inRange(hsv_image, lower, upper)
	cntr = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntr = imutils.grab_contours(cntr)
	output = image.copy()

	for c in cntr:
		c = max(cntr, key=cv2.contourArea)
		(x, y, w, h) = cv2.boundingRect(c)

	text = "The {} block is found!".format(color_names[index])

	index += 1

	cv2.putText(output, text, (10, 25), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)
	cv2.rectangle(output, (x,y),(x+w, y+h), (0, 0, 255), 2)

	# for c in cntr:
	# 	 cv2.drawContours(output, [c], -1, (255, 255, 159), 2)

	# output = cv2.bitwise_and(hsv_image, hsv_image, mask=mask)

	cv2.imshow("Lego Block Finder", output)
	cv2.waitKey(0)