import numpy as np
import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread("image1.PNG", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("", cv2.IMREAD_COLOR)
img_blur = cv2.medianBlur(img_gray, 9)

th1 = cv2.threshold(img_blur, 128, 255, cv2.THRESH_BINARY)

#image, contours, _ = cv2.findContours(th1.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#frame = cv2.drawContours(img_color, contours, -1, (0,0,0), 10)
#cv2.imwrite("aunp/aunp", frame)

plt.imshow(th1) #matplotlibは疑似カラーに自動で表示するため灰色を指定
plt.colorbar() #カラーバーを表示
plt.xticks([]) #[]でグラフのX軸を非表示
plt.yticks([]) #[]でグラフのY軸を非表示
plt.show()
