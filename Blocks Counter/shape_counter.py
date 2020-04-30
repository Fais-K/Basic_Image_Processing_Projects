import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# cv2.imshow("Original Image", image)
# cv2.waitKey(0)

grayed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray Image", grayed)
# cv2.waitKey(0)

# edged = cv2.Canny(grayed, 30, 150)
# cv2.imshow("Edge Detected", edged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

thresh = cv2.threshold(grayed, 240, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow("Threshed", thresh)
# cv2.waitKey(0)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts:
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)

# cv2.imshow("output", output)
# cv2.waitKey(0)

text = "Found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)
	
