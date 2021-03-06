#!/usr/bin/env python3
from PIL import Image
import os, sys

path = ('.')

def resize():
    for item in os.listdir(path):
        if os.path.isfile(item):
            im = Image.open(item)
            f, e = os.path.splitext(item)
            imResize = im.resize((1300,1200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

resize() 
