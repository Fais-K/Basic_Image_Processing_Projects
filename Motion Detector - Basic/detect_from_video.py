import numpy as np 
import argparse
from imutils.video import FileVideoStream
import imutils
import datetime
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to the video")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area")
args = vars(ap.parse_args())

fvs = FileVideoStream(args["video"]).start()
time.sleep(1)

# print(fvs.stream.get(cv2.CAP_PROP_FPS))

# first_frame = None
avg = None

while fvs.more():
	frame = fvs.read()
	text = "Unoccupied"

	scale_percent = 80
	width = int(frame.shape[1] * scale_percent / 100)
	height = int(frame.shape[0] * scale_percent / 100)
	dim = (width, height)

	frame = cv2.resize(frame, dim)
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# gray_frame = np.dstack([gray_frame, gray_frame, gray_frame])
	gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

	# if first_frame is None:
	# 	first_frame = gray_frame
	# 	continue

	if avg is None:
		avg = gray_frame.copy().astype("float")
		continue

	cv2.accumulateWeighted(gray_frame, avg, 0.5)
	frame_delta = cv2.absdiff(gray_frame, cv2.convertScaleAbs(avg))
	# frame_delta = cv2.absdiff(first_frame, gray_frame)
	thresh = cv2.threshold(frame_delta, 20, 255, cv2.THRESH_BINARY)[1]
	thresh = cv2.dilate(thresh, None, iterations=5)

	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)

	for c in cnts:
		if cv2.contourArea(c) < args["min_area"]:
			continue

		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
		text = "Occupied"

	if text == "Occupied":
		cv2.putText(frame, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	else:
		cv2.putText(frame, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)

	cv2.imshow("Security Feed", frame)

	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

fvs.stop()