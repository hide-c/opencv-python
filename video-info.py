import cv2
import os
import dlib
from tkinter import filedialog

os.chdir("ignore")
dir = os.getcwd()
video = cv2.VideoCapture(
    filedialog.askopenfilename(initialdir=dir)
    )

print("WIDTH=",int(video.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("HEIGHT=",int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("frame_count =",int(video.get(cv2.CAP_PROP_FRAME_COUNT)))
print("frame_rate = ",int(video.get(cv2.CAP_PROP_FPS)))
print(f"length: {video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)} s")
print("fourcc: " + int(video.get(cv2.CAP_PROP_FOURCC)).to_bytes(4, "little").decode("utf-8"))