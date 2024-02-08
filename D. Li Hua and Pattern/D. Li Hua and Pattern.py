pattern=[]
for _ in range(int(input())):
    pattern_size,k=map(int,input().split())
    for i in range(pattern_size):
        pattern.append(list(map(int,input().split())))
    count=0
    for i in range(pattern_size//2):
        for j in range(pattern_size):
            if pattern[i][j]!=pattern[pattern_size-i-1][pattern_size-j-1]:
                count+=1
            if count>k:
                break
        if count>k:
            break
    print(count)
    if count>k:
        print("no")
    elif((k-count)%2)==0:
        print("yes")

        