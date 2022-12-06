import numpy as np

def quadtree(img, x, y, w, h, threshold):
    if w <= 90 or h <= 60:
        return x
    if (((np.var(img[y:y+h, x:x+w]))**(0.5) < threshold)):
        return 1000*1000
    else:
        return min(quadtree(img, x, y, w//2, h//2, threshold),
                   quadtree(img, x+w//2, y, w-w//2, h//2, threshold),
                   quadtree(img, x, y+h//2, w//2, h-h//2, threshold),
                   quadtree(img, x+w//2, y+h//2, w-w//2, h-h//2, threshold))

