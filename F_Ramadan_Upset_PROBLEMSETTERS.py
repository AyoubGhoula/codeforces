
n,m=map(int,input().split())
a=sorted(map(int,input().split()))
b=list(map(int,input().split()))

res =[]
for x in b:
    f=0
    l=n
    while f < l:
        mid=(f+l)//2
        if a[mid]<=x:
            f=mid+1
        else:
            l=mid
    res.append(f)

print(' '.join(map(str,res)))
