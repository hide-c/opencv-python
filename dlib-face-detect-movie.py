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

#画像解析対象の画像を選択
os.chdir("ignore")
dir = os.getcwd()
video = cv2.VideoCapture(
    filedialog.askopenfilename(filetypes=[("AVI",".AVI")],initialdir=dir)
    )

#動画の情報取得
# 幅と高さを取得
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

#サイズが大きいと処理できない（GPUの性能が原因？）ため、サイズを制限
if width > 500:
    height = int(height * 500/width)
    width = 500
if height > 500:
    width = int(width * 500/width)
    height = 500

size = (width, height)

#総フレーム数を取得
frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
#フレームレート(1フレームの時間単位はミリ秒)の取得
frame_rate = int(video.get(cv2.CAP_PROP_FPS))

#保存
#fmt = cv2.VideoWriter_fourcc('P','I','M','1') # ファイル形式(ここではavi)
fmt = cv2.VideoWriter_fourcc('m','p','4','v') # ファイル形式(ここではmp4)
writer = cv2.VideoWriter('test.mp4', fmt, frame_rate, size) # ライター作成

for i in range(frame_count):
    ret, frame = video.read()
    if not ret:
        print("画像を正しく読み込めませんでした")
        break
    #顔検出
    frame = cv2.resize(frame,(int(width),int(height)))
    faces = detector(frame,1)

# 顔検出で得られた顔（複数あり得る）それぞれについて、四角を書く
    for i, f in enumerate(faces):
        box_label(frame, f.rect.left(), f.rect.top(), f.rect.right(), f.rect.bottom(), 'face')

    writer.write(frame)
writer.release()
video.release()
cv2.destroyAllWindows()

