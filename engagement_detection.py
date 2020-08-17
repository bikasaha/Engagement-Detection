# Run this file on CV2 in local machine to construct a Concentration Index (CI).
# Video image will show emotion on first line, and engagement on second. Engagement/concentration classification displays either 'Pay attention', 'You are engaged' and 'you are highly engaged' based on CI. Webcam is required.
# Analysis is in 'Util' folder.


from util.analysis_realtime import analysis
import cv2
import numpy as np
import csv



#CSV file initializing :

filename = "f.csv"
row_contents = ['x','y','time']

with open(filename, 'w', newline='') as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["y", "x","time"])


# Initializing

#cap = cv2.VideoCapture('VID_20200612_105442.mp4')
cap = cv2.VideoCapture(0)
ana = analysis()

# Capture every frame and send to detector
while True:
    _, frame = cap.read()
    bm = ana.detect_face(frame)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
# Exit if 'q' is pressed
    if key == ord('q'):
        break

# Release the memory
cap.release()
cv2.destroyAllWindows()
