import math

def partition(ar, N, K, idx, cmax):
    global ans
    s=0
    if K==1:
        s = sum(ar[idx:N])
        cmax= max(cmax, s)
        ans = min(ans, cmax)
    
    for i in range(idx, N-1):
        s= s+ar[i]
        cmax= max(cmax, s)
        partition(ar, N, K-1, i+1, cmax)


T= int(input())
for i in range(T):
    y = [int(x) for x in input().split()]
    N, K= y[0], y[1]
    K=min(N, K)
    ar= [int(x) for x in input().split()]
    ans= math.inf
    partition(ar, N, K, 0, 0)
    print(ans)
