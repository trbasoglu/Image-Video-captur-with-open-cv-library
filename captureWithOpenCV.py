import numpy as np
from datetime import datetime
import cv2

cap = cv2.VideoCapture(0)

video_capturing = False
while(True):
    _, frame = cap.read()
    if video_capturing:
        print("frame written")
        out.write(frame)
        cv2.putText(frame, "Recording", (100, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                    (255, 255, 255), 2, 5)
    nameofImg = "img_" + str(datetime.now().strftime('%d%m%y%H%M%S%f')) + '.jpg'  # name of video includes date and time
    cv2.imshow('original', frame)
    k = cv2.waitKey(1) & 0xff
    if k == 32:
        print("Image saving.")
        cv2.imwrite(nameofImg, frame)
        print("Image saved.")
    if k == ord('v'):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        nameofVid = "vid_" + str(datetime.now().strftime('%d%m%y%H%M%S%f')) + '.avi'
        out = cv2.VideoWriter(nameofVid, fourcc, 20.0, (640, 480))
        video_capturing = True
    if k == ord('s'):
        out.release()
        video_capturing = False
    if k == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()