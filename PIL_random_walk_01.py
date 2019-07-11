#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:17:05 2019

@author: timallan
"""


from PIL import Image, ImageDraw
import random

#im = Image.open('/Users/timallan/Desktop/whiteFang/01_ASSETS/__IMAGES/_DL/northernLights_1920x1080.png')

im = Image.new('RGB', (1920, 1080), ('black'))

w, h = im.size

pixelTotal = w * h
pixelTarget = int(pixelTotal * .41)

pointsDrawn = 0
pointsDrawnList = []

x = random.randrange(w)
y = random.randrange(h)

draw = ImageDraw.Draw(im)


for points in range(pixelTarget):
    choice = random.randrange(4)
    
    if x < 0 or x > w:
            x = 0
    if y < 0 or y > h:
            y = 0
            
    if choice == 0:
        x += 1
        draw.point((x, y), fill = ('white'))
        pointsDrawnList.append(y)
        pointsDrawnList.append(x)
        
    elif choice == 1:
        x -= 1
        draw.point((x, y), fill = ('white'))
        pointsDrawnList.append(y)
        pointsDrawnList.append(x)
        
    elif choice == 2:
        y += 1
        draw.point((x, y), fill = ('white'))
        pointsDrawnList.append(y)
        pointsDrawnList.append(x)
    
    elif choice == 3:
        y -= 1
        draw.point((x, y), fill = ('white'))
        pointsDrawnList.append(y)
        pointsDrawnList.append(x)
        
del draw
print( len(pointsDrawnList) / 2 )

im.save('/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/_GENERATED_IMAGES/1920x1080_random_walk_06.png', 'PNG')           
im.show() 
