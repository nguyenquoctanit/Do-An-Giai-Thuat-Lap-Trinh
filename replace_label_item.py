import glob
import cv2
import os
path = "D:/TEST/CAM4/*.txt"

for i in glob.glob(path):
    label_new = []
    if i[-11:] == "classes.txt":
        continue

    # Modify the x values in the file
    with open(i, "r") as file:
        Lines = file.readlines()
        for line in Lines:
            if line == "":
                continue
            if int(line.strip().split(" ")[0]) == 14 and float(line.strip().split(" ")[2]) > 0.5:
                line = "14 0.672386 0.693359 0.120915 0.207031\n"

            label_new.append(line)


    with open(i, 'w') as f:
        for line in label_new:
            f.write(line)
