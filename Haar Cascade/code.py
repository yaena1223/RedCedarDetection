import os
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import json

path_dir = './'
txt_list = []
jpg_list = []
for file in os.listdir(path_dir):
    if "txt" in file: 
        if "converted" not in file:
            txt_list.append(file)
    if "jpg" in file:
        jpg_list.append(file)

# print("txt_list :", txt_list)
# print("jpg_list :", jpg_list)

result = []
for txtFile in txt_list:
    txtPath = path_dir + txtFile

    # Opening Txt file
    file = open(txtPath, 'r')
    Lines = file.readlines()
    
    print("\n[+] {} Start!".format(txtFile))
    img = cv2.imread(txtPath[:-4] + ".jpg", cv2.IMREAD_COLOR)
    
    count = 0
    haar_coord = ""
    # Strips the newline character
    for line in Lines:
        count += 1
        words = line.split()
        (classes, xcenter, ycenter, w, h) = list(map(float, words))
#         print(int(classes), xcenter, ycenter, w, h)
        (h_img, w_img, _) = img.shape
        (rect_h, rect_w) = (int(h * h_img), int(w * w_img))
        (xmin, ymin) = (int(xcenter * w_img - (rect_w / 2)), int(ycenter * h_img - (rect_h / 2)))
        if xmin < 0 or ymin < 0 or xmin >= w_img or ymin >= h_img or rect_w == 0 or rect_h == 0:
            print("Problem!!! [xmin :", xmin, "ymin :", ymin, "rect_w :", rect_w, "rect_h :", rect_h, "]")
#         print("h_img :", h_img, "w_img :", w_img, "xmin :", xmin, "ymin :", ymin)
#         image = cv2.rectangle(img, (xmin, ymin), (xmin + rect_w, ymin + rect_h), (255, 255, 255), 3)
        haar_coord += " {} {} {} {} ".format(xmin, ymin, rect_w, rect_h)
        
    gatheredLine = "{} {}".format(txtPath[:-4] + ".jpg", count) + haar_coord + '\n'

    print("gatheredLine : ", gatheredLine)
    result.append(gatheredLine)
#     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # Because OpenCV stores images in BGR order instead of RGB.
#     plt.show()
    print("[-] {} DONE!\n".format(txtFile))
    
with open(path_dir + "converted.txt", 'w') as f:
    for line in result:
        f.write(line)

print("[ !!!END!!! ]")