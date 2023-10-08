#!/usr/bin/env python3
from PIL import image
import os

for img  in os.listdir("images/"):
    if img != ".DS_Store":
        im = Image.open(os.path.join("images/", img))
        im = im.rotate(90).resize(128,128).save(os.path.join("new_images", img))
        
