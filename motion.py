import cv2
cap=cv2.VideoCapture(0) #0 for internal lappy camera 1 for external camera

tp1=cap.read()[1] #take1
tp2=cap.read()[1] #take2
tp3=cap.read()[1] #take3
#to make more perfect
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY) # converting into gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY) # converting into gray
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY) # converting into gray

#now creating image diff
def img_diff(x,y,z):
	#diff between x and y or diff between gray1 and gray2  ---d1
	d1=cv2.absdiff(x,y)
	#diff between y and z or diff between gray2 and gray3 ----d2
	d2=cv2.absdiff(y,z)
	#absolute difference -- d1 and d2
	finalimg=cv2.bitwise_and(d1,d2)
	return finalimg 

#now apply function
while cap.isOpened():
	status,frame=cap.read()
	motion=img_diff(gray1,gray2,gray3)
	#replacing image frame
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
	cv2.imshow('motion',motion)
	#cv2.imshow
	if cv2.waitKey(5) & 0xff == ord('q') :
		break
cv2.destroyAllWindows()
cap.release()		