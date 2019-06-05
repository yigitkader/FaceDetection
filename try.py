import cv2
import numpy as np


#Kameradan görüntü alıyoruz.
camera= cv2.VideoCapture(0)

#face_cascade=cv2.CascadeClassifier('haarcascade_profile.xml')
#frontal_face_cascade=cv2.CascadeClassifier('frontal_face.xml')
frontal_face_extended=cv2.CascadeClassifier('frontal_face_extended.xml')


""" Ret will obtain return value from getting the camera frame, either true or false """
while(1):
	
	ret,frame=camera.read()

	grey_ton = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Convertcolor(cvtColor)

	#faces=face_cascade.detectMultiScale(grey_ton,1.1,2)  # skalama oranı, minumum komsuluk(kac tane yüz var teyit et)
	
	faces=frontal_face_extended.detectMultiScale(grey_ton,1.1,2)
	
	for(x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3) #framei göster,sol üst ,sağ üst koordinatla,renk,kalınlık


	# for(x,y,w,h) in faces:
	# 	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)		

	# for(x,y,w,h) in faces2:
	# 	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)


	cv2.imshow('original',frame)

	if cv2.waitKey(25) & 0xFF ==ord('q'):
		break


camera.release()
cv2.destroyAllWindows()
	


	# resimi gri yapmak islemciden hız kazanmak ve isi daha cabuk yapmak icin kullanılır yoksa yine de calısır renkli.