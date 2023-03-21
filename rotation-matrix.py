import numpy as np
import matplotlib.pyplot as plt
import cv2
import random



image = cv2.imread('')#img

for i in range(image.shape[0]):
    image[i,:,:] = [random.randint(0, 255) for _ in range(3)]

xyaxis = []

array_y = 0
for y in range(int((image.shape[0]-1)/2), int(-1*(image.shape[0]+1)/2), -1):
    array_x = 0
    for x in range(int(-1*(image.shape[0]-1)/2), int((image.shape[0]+1)/2)):
        xyaxis.append((x, y, array_x, array_y))
        
        array_x += 1

    array_y += 1


print (xyaxis)
