import cv2
def takePhoto():
    # przykładowe dane kamery
	host = '192.168.43.20'
	stream = '1'
	username = 'admin'
	password = 'admin1'
	camera = cv2.VideoCapture('rtsp://'+username+':'+password+'@'+host+':554/live2.sdp')
	while True:
		return_value,image = camera.read()
		if not return_value:
			print("odczyt")
			break
		gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		cv2.imshow('image',gray)
		if cv2.waitKey(1):
			cv2.imwrite('photo.jpg',image)
			break
	camera.release()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	takePhoto()
