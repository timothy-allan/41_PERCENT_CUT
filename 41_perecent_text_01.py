#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 14:33:28 2019

@author: timallan
"""
import random

origFile = open('/Users/timallan/Desktop/whiteFang/WhiteFangOriginal.txt', 'r')
saveFile = open('/Users/timallan/Desktop/whiteFang/wF_03.txt', 'w')

origLines = origFile.readlines()

cutLines = []





for aLine in origLines:
    cutLine = []
    singleLineList = aLine.split()
    
    for aWord in singleLineList:
        
        randNum = random.randrange(0, 101)
        if randNum > 59:
            cutLine.append(aWord)
        cutString = ' '.join(cutLine)
        
    cutLines.append(cutString)

cutFinalString = '\n'.join(cutLines)


print(cutFinalString)
print(len(cutFinalString))
saveFile.write(cutFinalString)

origFile.close()
saveFile.close()
