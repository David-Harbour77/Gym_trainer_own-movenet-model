import utils
from ml import Movenet
import cv2
import time
movenet = Movenet('movenet_thunder')

pTime = 0
cap = cv2.VideoCapture("3.mp4")

count = 0.5
dir = 0
angle = 0
while (cap.isOpened()):
  ret, frame = cap.read()
  frame = cv2.resize(frame, (600,800))
  person = movenet.detect(frame)
  image,count,dir,angle = utils.visualize(angle,count,dir, frame, [person])
  cTime = time.time()
  fps = 1 / (cTime - pTime)
  pTime = cTime
  cv2.putText(image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
  cv2.imshow('1', image)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
                              
                          