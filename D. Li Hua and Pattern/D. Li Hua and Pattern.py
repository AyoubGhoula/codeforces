for _ in range(int(input())):
    pattern=[]
    pattern_size,k=map(int,input().split())
    for i in range(pattern_size):
        pattern.append(list(map(int,input().split())))
    count=0
    if pattern_size%2==0:
        n=pattern_size//2
    else:
        n=(pattern_size//2)+1
    for i in range(n):
        for j in range(pattern_size):
            if i ==n-1 and j==n-1 and pattern_size%2!=0:
                break
            if pattern[i][j]!=pattern[pattern_size-i-1][pattern_size-j-1]:
                count+=1
            if count>k:
                break
        if count>k:
            break
    if count>k:
        print("no")
    elif((k-count)%2)==0:
        print("yes")

        