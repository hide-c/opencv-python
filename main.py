import cv2
import os
from tkinter import filedialog

#画像解析対象の画像を選択
os.chdir("ignore")
dir = os.getcwd()
img = cv2.imread(
    filedialog.askopenfilename(filetypes=[("JPG",".jpg")],initialdir=dir)
    )

#グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#顔検出器の定義
face_cascade_path = 'haarcascade_frontalface_default.xml'

#顔検出器の読み込み
face_cascade = cv2.CascadeClassifier(face_cascade_path)

#顔検出実施して、その場所を四角形の枠線で囲む
faces = face_cascade.detectMultiScale(gray)
for x, y, w, h in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#画像保存
cv2.imwrite('face-detect.jpg',img)
