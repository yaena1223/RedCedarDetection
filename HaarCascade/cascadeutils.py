import os
import cv2 
from PIL import Image
def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('./neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('./image/n'):
            f.write('image/n/' + filename + '\n')


def generate_positive_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('./txt/redcedar_polygon.txt', 'w') as g:
        # loop over all the filenames
        files = os.listdir('./image/redcedar')
        for file in files:
            img = Image.open(os.path.join('./image/redcedar', file))
            w, h = img.size
            g.write('../image/redcedar/' + file+ " 1 0 0 "+ str(w) + " "+ str(h)+'\n')


=

