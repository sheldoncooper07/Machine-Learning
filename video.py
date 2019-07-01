import cv2
cap=cv2.VideoCapture(0) #0 for internal lappy camera 1 for external camera
plugin=cv2.VideoWriter_fourcc(*"XVID") #adding plugin
output=cv2.VideoWriter("a.avi",plugin,100,(640,480)) #saving video #(width height)

while cap.isOpened():
	status,frame=cap.read()
	cv2.imshow('ilive',frame)
	output.write(frame) #sending  data to video writer86
	if cv2.waitKey(5) & 0xff == ord('q') :
		break
cv2.destroyAllWindows()
cap.release()		