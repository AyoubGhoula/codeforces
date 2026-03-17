for _ in range(int(input())):
    a,b=map(int,input().split())
    nb=max(a,b)-min(a,b)
    if nb%10==0:
        print(nb//10)
    else:
        print((nb//10)+1)