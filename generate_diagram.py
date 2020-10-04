import cv2
import numpy as np
from tqdm import tqdm


WIDTH = 3840*2
HEIGHT = 2160*2
img = np.ones((HEIGHT, WIDTH, 4))
BG_COLOR = np.array([33, 37, 41, 1])
img *= BG_COLOR
img[:, :, 3] = 255
# Some asthetic gaussian noise
img[:, :, :3] += (3*np.random.randn(HEIGHT, WIDTH, 3)).astype(int)

R = np.linspace(2, 4, 10001)
N = 100
for r in tqdm(R):
    x = 0.000001
    for i in range(10*N):
        if i >= 8*N:
            coordinate = (int((r-2)/2*WIDTH), int((1-x)*HEIGHT))
            img = cv2.circle(img, coordinate, 1, color=(53, 191, 92, 200),
                             thickness=-1)
        x = r*x*(1-x)

img = cv2.blur(img, (3, 3))
cv2.imwrite('test.png', img)
