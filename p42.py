import numpy as np 
import math as m 


with open('/Users/xueyishu/Downloads/p042_words.txt','r') as f:
    words = f.read().split(',')
    words = [list(word.strip('\"')) for word in words]
    f.close()

def istriangle(n):
    x = (m.sqrt(8*n + 1) - 1) / 2
    if x - int(x) > 0: # if x is not an integer
        return False
    else:
        return True 


def findloc(word):
    loc = 0
    s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in word:
        loc += s.index(i) + 1
    return loc 


count = 0

for i in range(len(words)):
    temp = words[i]
    num = findloc(temp)
    if istriangle(num) == True:
        count += 1

print count
