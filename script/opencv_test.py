"""Explore the functions in bioinspired module.

Duplicate basicRetina.cpp

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import cv2
from cv2 import bioinspired

cap = cv2.VideoCapture(0)
retina = bioinspired.createRetina((512, 512))

retina.clearBuffers()

while (True):
    ret, frame = cap.read()

    dsize = frame.shape
    frame = cv2.resize(frame, (512, 512))

    retina.run(frame)
    retina_output_parvo = retina.getParvo()
    retina_output_magno = retina.getMagno()

    cv2.imshow("frame", frame)
    cv2.imshow("Parvo", retina_output_parvo)
    cv2.imshow("Magno", retina_output_magno)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
