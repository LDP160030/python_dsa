import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a= sorted(a)
    n= len(a)
    sublist=[]
    p1=0
    p2=1
    p1_next=1
    while p2<n and p1<n-1:
        if (a[p2]-a[p1])==0:
            p2 += 1
            p1_next=p2
        elif (a[p2]-a[p1])==1:
            p2 += 1
        else:
            sublist.append(a[p1:p2])
            p1= max(p1+1, p1_next)
            p2 = p1+1
            p1_next=p1
            print(p1_next)
    if len(sublist)==0:
        return(len(a))
    else:
        sublist.append([1, 2])
    return max([len(x) for x in sublist])
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
