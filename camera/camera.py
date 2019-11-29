import cv2

# przykładowe dane kamery
host = '192.168.0.20'
stream = '1'
username = 'admin'
password = 'admin1'

camera = cv2.VideoCapture('rtsp://'+username+':'+password+'@'+host+':80/')
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('photo.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()

# https://www.epiphan.com/userguides/pearl/Content/UserGuides/Streaming/capture/sourceIPCameras.htm

#https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv
