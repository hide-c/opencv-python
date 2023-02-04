import cv2
import os
import dlib
from tkinter import filedialog

def box_label(img, x1, y1, x2, y2, label): 
    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 1, 1)
    cv2.rectangle(img, (int(x1), int(y1-25)), (x2, y1), (255,255,255), -1)
    cv2.putText(img, label, (x1, int(y1-5)), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 1)

# 顔検出器を取得
#detector = dlib.get_frontal_face_detector()
datfile = "/usr/share/dlib/mmod_human_face_detector.dat"
detector = dlib.cnn_face_detection_model_v1(datfile)

#cameraから画像取得
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    cv2.waitKey(1)
    ret, frame = cap.read()
    if not ret:
        print("画像を正しく読み込めませんでした")
        break
    #顔検出
    faces = detector(frame,1)

# 顔検出で得られた顔（複数あり得る）それぞれについて、四角を書く
    for i, f in enumerate(faces):
        box_label(frame, f.rect.left(), f.rect.top(), f.rect.right(), f.rect.bottom(), 'face')
    cv2.imshow("camera",frame)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'): #qキーを押すと終了
        break

cap.release()
cv2.destroyAllWindows()