import argparse
import cv2
import numpy as np
import quadtree as qd
import glob
import os

img_dir = "test images"
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
data = []

for f1 in files:
    img = cv2.imread(f1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = qd.quadtree(img, 0, 0, len(img[0]), len(img), 48)
    print(f1,end= "  ")
    if len(img[0]) > x:
        print("Good image")
    else:
        print("Bad image")
print()
print()
for f1 in files:
    img = cv2.imread(f1)
    print(f1,end= "  ")
    if ((np.var(img))**(0.5) < 53):
        print("Bad image")
    else:
        print("Good image")
        