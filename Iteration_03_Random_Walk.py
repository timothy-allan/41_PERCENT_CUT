#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:17:05 2019

@author: timallan
"""
'''
runfile('/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK/PIL_random_walk_05.py', wdir='/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK')
1910.6162600517273
125951 125951 983621 857670
save file - 300x300_random_walk_01.png

runfile('/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK/PIL_random_walk_05.py', wdir='/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK')
6895.042726993561
196800 196800 2256973 2060173
save file - 640x480_random_walk_01.png

runfile('/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK/PIL_random_walk_05.py', wdir='/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK')
13975.19358086586
322437 322437 2313861 1991424
save file - 1024x768_random_walk_01.png1024x768

runfile('/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK/PIL_random_walk_05.py', wdir='/Users/timallan/Desktop/whiteFang/05_CODE/PYTHON/PIL/RANDOM_WALK')
390868.6569070816
850176 850176 8270217 7420041
save file - 1920x1080_random_walk_01.png

'''



from PIL import Image, ImageDraw
import random
import time

#im = Image.open('/Users/timallan/Desktop/whiteFang/01_ASSETS/__IMAGES/_DL/northernLights_1920x1080.png')

im = Image.new('RGB', (200, 200), (240, 240, 240))

w, h = im.size

pixelTotal = w * h
pixelTarget = int(pixelTotal * 0.41)

pointsDrawn = 0
pointsDrawnList = []

x = random.randrange(w)
y = random.randrange(h)
steps = 0

draw = ImageDraw.Draw(im)

startTime = time.time()


while pointsDrawn < pixelTarget:
    

    
    steps += 1

        
    if (x, y) not in pointsDrawnList:
            
        draw.point((x, y), (5, 5, 5))
        pointsDrawnList.append((x, y))
        pointsDrawn +=1    
        
            
    stepx = random.randrange(-1, 2)
    stepy = random.randrange(-1, 2)
    
     
    x += stepx
    y += stepy  
    
    
    if x < 0 or x > w: x = 0
    if y < 0 or y > h: y = 0
        
        

     
del draw

endTime = time.time()
elapsedTme = endTime - startTime

print(elapsedTme)
print(pointsDrawn, pixelTarget, steps, steps-pixelTarget)

#im.save('/Users/whiteFang/05_CODE/_GENERATED_IMAGES/1920x1024_random_walk_01.png', 'PNG') 
       
im.show() 
