import cv2
cap=cv2.VideoCapture(0) #0 for internal lappy camera 1 for external camera

while cap.isOpened():
	status,frame=cap.read()
	#detecting red  color
	redimg=cv2.inRange(frame,(0,0,0),(40,40,255))
	cv2.imshow('iliveredcolor',redimg)
	if cv2.waitKey(5) & 0xff == ord('q') :
		break
cv2.destroyAllWindows()
cap.release()		