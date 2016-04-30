"""This script is in charge of creating figures.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import os
from os.path import join
import cv2
from cv2 import bioinspired

data_path = os.environ["SIMRETINA_DATA"]

option = "lenna-figure"

if option == "lenna-figure":
    lenna = cv2.imread(join(data_path, "lenna.png"))
    retina = bioinspired.createRetina((lenna.shape[0], lenna.shape[1]))
    retina.clearBuffers()

    retina.run(lenna)
    lenna_output_parvo = retina.getParvo()
    lenna_output_magno = retina.getMagno()

    cv2.imwrite(join(data_path, "lenna_parvo.png"), lenna_output_parvo)
    cv2.imwrite(join(data_path, "lenna_magno.png"), lenna_output_magno)

    print "Output is written to %s" % (data_path)
