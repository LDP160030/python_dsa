# 100 monkey doors
def monkeydoors(m, n):
    #as first monkey open all doors
    doors=['o']*n
    #dummy first element
    doors.insert(0, 'k')
    i=2
    while i<=m:
        for j in range(i, n+1, i):
            if doors[j]=='c':
                doors[j]='o'
            else:
                doors[j]='c'
        i=i+1
    sum=0
    for i in range(1, n+1):
        if doors[i]=='o':
            sum= sum+1
    return(sum)
