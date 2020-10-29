import numpy as np
import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread("image1.PNG", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("image1.PNG", cv2.IMREAD_COLOR)
img_blur = cv2.medianBlur(img_gray, 5)

r, th1 = cv2.threshold(img_blur, 128, 255, cv2.THRESH_BINARY)


plt.imshow(th1, 'gray') 
plt.colorbar() 
plt.xticks([]) 
plt.yticks([]) 
plt.show()