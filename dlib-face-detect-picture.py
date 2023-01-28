import cv2
import os
import dlib
from tkinter import filedialog

# 顔検出器を取得
detector = dlib.get_frontal_face_detector()

#画像解析対象の画像を選択
os.chdir("ignore")
dir = os.getcwd()
img = cv2.imread(
    filedialog.askopenfilename(filetypes=[("JPG",".jpg"),("JPG",".JPG")],initialdir=dir)
    )

#グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#顔検出
faces = detector(img)

#顔検出実施して、その場所を四角形の枠線で囲む
for face in faces:

# rectangle visualize
    img_rec = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),
            color=(255, 255, 255), lineType=cv2.LINE_AA, thickness=2)

#画像保存
cv2.imwrite('face-detect-dlib.jpg',img)
