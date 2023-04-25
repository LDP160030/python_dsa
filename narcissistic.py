MOD= 1000000007

def Narcissistic(n):
    k= len(str(n))
    newnumber= n
    sum1=0
    while newnumber!=0:
        remainder= newnumber%10
        sum1 = sum1+(power(remainder, k))
        sum1= sum1%MOD
        newnumber= newnumber//10
    if sum1==n:
        return('Yes')
    else:
        return('No')
    

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power((a * a) % MOD, b // 2)
    else:
        return (a * power((a * a) % MOD, (b - 1) // 2)) % MOD
        

n= int(input())
print(Narcissistic(n))
