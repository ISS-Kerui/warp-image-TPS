import numpy as np
import cv2

def WarpImage_TPS(source,target,img):
	tps = cv2.createThinPlateSplineShapeTransformer()
	
	print source
	print target
	source=source.reshape(-1,len(source),2)
	target=target.reshape(-1,len(target),2)

	matches=list()
	for i in range(0,len(source[0])):

		matches.append(cv2.DMatch(i,i,0))

	tps.estimateTransformation(target,source,matches)
	new_img = tps.warpImage(img)
	return new_img

