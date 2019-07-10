#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:17:05 2019

@author: timallan
"""

from PIL import Image, ImageDraw
import random

im = Image.open('/Users/timallan/Desktop/whiteFang/01_ASSETS/__IMAGES/_DL/northernLights_1920x1080.png')
w, h = im.size

pixelTotal = w * h
pixelTarget = int(pixelTotal * 0.41)

pointTotal = 1
x_pos = 0
width_adjust = 184          
flip = False                

draw = ImageDraw.Draw(im)

while pointTotal <= pixelTarget:
    y_length = random.randrange(0, h - width_adjust)
    
    for y in range(y_length):
        
        if pointTotal <= pixelTarget:
            
            if flip:
                draw.point((x_pos, y), fill = ('white'))
                pointTotal += 1
            
            else:
                draw.point((x_pos, h - y), fill = ('white'))
                pointTotal += 1
                
    x_pos += 1       
    flip = not flip          

del draw

im.save('/Users/timallan/Desktop/whiteFang/01_ASSETS/__IMAGES/_DL/northernLights_1920x1080_VERT_ALTERNATE_01.png', 'PNG')           
im.show() 
