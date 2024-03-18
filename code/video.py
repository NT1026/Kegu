import cv2
WIDTH = 1280
HEIGHT = 720
cap = cv2.VideoCapture('https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=10002&0.7547919814792337')

while (cap.isOpened()):
    ret, frame = cap.read()
    if type(frame) == type(None):
        break
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()