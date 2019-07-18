#!/usr/bin/env python
# import the necessary packages
import numpy as np
import argparse
import sys
import cv2
 
photo = sys.argv[1]

# load the image
image = cv2.imread(photo)

# find all the 'black' shapes in the image
lower = np.array([0, 0, 0])
upper = np.array([50, 50, 50])
shapeMask = cv2.inRange(image, lower, upper)

# find the contours in the mask
contours, _= cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
epsilon = 0.01*cv2.arcLength(contours[0],True)
approx = cv2.approxPolyDP(contours[0],epsilon,True)

# hg bg bd hd
for p in approx:
	sys.stdout.write(str(p[0][0]) + '@' + str(p[0][1]) + '!')
