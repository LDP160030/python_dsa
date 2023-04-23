import math

def valid(ar, N, K, mid):
    currentval= 0
    countofperson=1
    for i in range(N):
        if (currentval+ar[i])<=mid:
            currentval += ar[i]
        else:
            countofperson += 1
            currentval= ar[i]
    if countofperson<=K:
        return True
    else:
        return False    

def partition_bs(ar, N, K):
    sum1=0
    for i in ar:
        sum1 += i
    low=max(ar)
    high= sum1
    while low<=high:
        mid= low+(high-low)//2
        if valid(ar, N, K, mid):
            ans= mid
            high= mid-1
        else:
            low= mid+1
    return ans
        
T= int(input())
for i in range(T):
    y = [int(x) for x in input().split()]
    N, K= y[0], y[1]
    K=min(N, K)
    ar= [int(x) for x in input().split()]
    print(partition_bs(ar, N, K))
