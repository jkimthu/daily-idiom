#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
RANDOM IDIOM GENERATOR

1. Run code to print a randomly assigned idiom from The List.
2. Once assigned, the idiom is removed from those available for sampling.
3. Thus an idiom is never randomly assigned twice.

Created on Sat Apr 18 20:58:00 2020
@author: jen

"""


# 0. import numpy and pickle
import numpy as np


# 1. import list of idioms from remaining collection
with open('remaining.py') as f:
    idioms = f.read().splitlines()

#import subprocess
#subprocess.Popen("/Users/jen/daily-idiom/collection.py", shell=True)
#from collection import idioms
# print(len(idioms))
# print(type(idioms))
# print(idioms)



# 1. define low (inclusive) and high (exclusive) ends of list
lowNum = 0;
highNum = len(idioms)-1;
# print(lowNum)
# print(highNum)


# 2. print a random idiom from list
idioNum = np.random.randint(lowNum,highNum)
print(idioNum)
print(idioms[idioNum])


# 3. edit collection to remove assigned idiom from list
idioms.remove(idioms[idioNum])
#print(idioms)


# 4. save edited collection for future use
#    if using 1B, these lines will re-write remainder.py
#    with one less string element than we started with
with open('remaining.py', 'w') as fh:
    for i in idioms:
        fh.write(i + '\n')

        
    

