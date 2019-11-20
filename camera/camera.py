import cv2

# przykładowe dane kamery
scheme = '192.168.1'
stream = '1'
username = 'admin'
password = 'admin'

host = scheme+'101'
camera = cv2.VideoCapture('rtsp://'+username+':'+password+'@'+host+':554/')
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