#!/usr/bin/python3

import sys
import csv

reader = csv.reader(open('test.txt','r'))

with open('test.txt','r') as file :
 wordDict = {}
 reader = csv.reader(file,delimiter=' ', quotechar='|')
 for line in reader :
  for element in line :
   words = element.split(' ')
   for word in words :
    if word not in wordDict.keys() :
     wordDict[word] = 1
    else :
     wordDict[word] = wordDict[word] + 1
print(wordDict)
