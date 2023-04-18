#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    countdict={}
    maxele=1
    for i in range(len(arr)):
        if arr[i] in countdict:
            countdict[arr[i]]= countdict[arr[i]]+1
            maxele = max(countdict[arr[i]], maxele)
        else:
            countdict[arr[i]]= 1
    maxlist= []
    for x, y in countdict.items():
        if y==maxele:
            maxlist.append(x)
    return sorted(maxlist)[0]
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
