import cv2
def takePhoto():
    # przykładowe dane kamery
    host = '192.168.0.20'
    port = ':80/'	#zmienić 
    stream = '1'
    username = 'admin'
    password = 'admin1'
	camera = cv2.VideoCapture('rtsp://'+username+':'+password+'@'+host+port)
	while True:
		return_value,image = camera.read()
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		cv2.imshow('image',gray)
		if cv2.waitKey(1)& 0xFF == ord('s'):
			cv2.imwrite('photo.jpg',image)
			break
	camera.release()
	cv2.destroyAllWindows()
