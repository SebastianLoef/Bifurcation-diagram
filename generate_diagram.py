#!/usr/bin/env python3
import argparse
import cv2
import numpy as np
from tqdm import tqdm


WIDTH = 3840*2
HEIGHT = 2160*2
BG_COLOR = (33, 37, 41)
DIAGRAM_COLOR = (53, 191, 92)


def generate_bg(width, height, color, noise=False):
    img = np.ones((height, width, 3))
    img *= np.array(color)
    if noise:
        # Some asthetic gaussian noise
        img += (3*np.random.randn(HEIGHT, WIDTH, 3)).astype(int)
    return np.clip(img, 0, 255)


def generate_diagram(bg, color, blur=False):
    img = bg
    height, width, _ = img.shape
    R = np.linspace(2, 4, 10001)
    N = 100
    for r in tqdm(R):
        x = 0.000001
        for i in range(10*N):
            if i >= 8*N:
                coordinate = (int((r-2)/2*width), int((1-x)*height))
                img = cv2.circle(img, coordinate, 1,
                                 color=color, thickness=-1)
            x = r*x*(1-x)

    if blur:
        img = cv2.blur(img, (blur, blur))
    cv2.imwrite('img.png', img)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--bg", default=None,
                        help="You can set an image as background to"
                        +    "the diagram. \nNote that this will disable"
                        +    "other background options")
    parser.add_argument("--bg_color", default=BG_COLOR,
                        help="Set a static background color")
    parser.add_argument("--bg_noise",  default=False,
                        help="Adds gaussian noise to the background")
    parser.add_argument("--diagram_color", default=DIAGRAM_COLOR,
                        help="Change the color of the diagram")
    parser.add_argument("--width", default=WIDTH,
                        help="Set width, this will be overwritten"
                        +    "by --bg option if set")
    parser.add_argument("--height", default=HEIGHT,
                        help="Set height, this will be overwritten"
                        +    "by --bg option if set")
    parser.add_argument("--blur", default=3,
                        help="Might make the picture look better.")

    args = parser.parse_args()

    if args.bg:
        bg = cv2.imread(args.bg)
    else:
        bg = generate_bg(args.width, args.height,
                         args.bg_color, args.bg_noise)
    generate_diagram(bg, args.diagram_color, args.blur)
