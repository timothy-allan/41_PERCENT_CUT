#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:33:28 2019

@author: timallan
"""
import random

origFile = open('/Users/timallan/Desktop/whiteFang/03_inDESIGN/_TXT/WhiteFangOriginal.txt', 'r')
saveFile = open('/Users/timallan/Desktop/whiteFang/03_inDESIGN/_TXT/wF_06.txt', 'w')

origLines = origFile.readlines()

origLineCount = len(origLines)
origWordCount = 0

cutLine = []
cutLines = []

for aLine in origLines:
    origWordCount += len(aLine)
      
   

for aLine in origLines:
    singleLine = aLine.split()
    origLineLen = len(singleLine)
    targetLineLen = int(origLineLen * 0.41)
        

    while origLineLen > targetLineLen:
        randNum = random.randrange(0, origLineLen)
        
        singleLine.pop(randNum)
        origLineLen -= 1
        
    cutString = ' '.join(singleLine)
        
    cutLines.append(cutString)

cutFinalString = '\n'.join(cutLines)


print(cutFinalString)
saveFile.write(cutFinalString)


origFile.close()
saveFile.close()
