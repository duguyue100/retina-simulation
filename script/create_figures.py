"""This script is in charge of creating figures.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import os
from os.path import join
import cv2
from cv2 import bioinspired
from moviepy.editor import ImageSequenceClip

from simretina import dataset

data_path = os.environ["SIMRETINA_DATA"]

# "lenna-figure"
# "gif-horse-riding"

option = "gif-horse-riding"

if option == "lenna-figure":
    frame, size = dataset.get_lenna()
    retina = bioinspired.createRetina(size)
    retina.clearBuffers()

    retina.run(frame)
    lenna_output_parvo = retina.getParvo()
    lenna_output_magno = retina.getMagno()

    cv2.imwrite(join(data_path, "lenna_parvo.png"), lenna_output_parvo)
    cv2.imwrite(join(data_path, "lenna_magno.png"), lenna_output_magno)

    print "Output is written to %s" % (data_path)

if option == "gif-horse-riding":
    frames, size = dataset.get_horse_riding()
    retina = bioinspired.createRetina((size[1], size[0]))
    retina.clearBuffers()

    video_save_path = join(data_path, "retina-simulation",
                           "horse-riding.gif")
    parvo_save_path = join(data_path, "retina-simulation",
                           "horse-riding-parvo.gif")
    magno_save_path = join(data_path, "retina-simulation",
                           "horse-riding-magno.gif")

    parvo_frames = []
    magno_frames = []
    origin_frames = []
    for frame in frames:
        retina.run(frame)

        origin_frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        parvo_frame = retina.getParvo()
        parvo_frame = cv2.cvtColor(parvo_frame, cv2.COLOR_BGR2RGB)
        parvo_frames.append(parvo_frame)
        magno_frames.append(retina.getMagno())

    clip = ImageSequenceClip(parvo_frames, fps=30)
    clip.write_gif(parvo_save_path, fps=30)
    print "[MESSAGE] Parvo frames is saved at: %s" % (parvo_save_path)

    clip = ImageSequenceClip(magno_frames, fps=30)
    clip.write_gif(magno_save_path, fps=30)
    print "[MESSAGE] Magno frames is saved at: %s" % (magno_save_path)

    clip = ImageSequenceClip(origin_frames, fps=30)
    clip.write_gif(video_save_path, fps=30)
    print "[MESSAGE] Original frames is saved at: %s" % (video_save_path)
