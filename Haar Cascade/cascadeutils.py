import os
import cv2 
from PIL import Image
def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('C:/HaarCascade/neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('C:/HaarCascade/image/n'):
            f.write('image/n/' + filename + '\n')


def generate_positive_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('C:/HaarCascade/txt/redcedar_polygon.txt', 'w') as g:
        # loop over all the filenames
        files = os.listdir('C:/HaarCascade/image/redcedar_polygon')
        for file in files:
            img = Image.open(os.path.join('C:/HaarCascade/image/redcedar_polygon', file))
            w, h = img.size
            g.write('../image/redcedar_polygon/' + file+ " 1 0 0 "+ str(w) + " "+ str(h)+'\n')


def generate_positive_description_file_yolo():
    # open the output file for writing. will overwrite all existing data in there
        files = os.listdir('C:/HaarCascade/positive')
        for file in files:
            file_name = os.path.splitext(file)[0]+".txt"
            img = Image.open(os.path.join('C:/HaarCascade/positive', file))
            g = open(file_name,'w')
            w, h = img.size
            g.write("1 0 0 "+ str(w) + " "+ str(h)+'\n')

