n=int(input())
for i in range(n):
    s=input()
    nb=s.count("?")
    if s[0]=="0":
        print(0)
    elif s[0]=="?":
        print(9*10**(nb-1))
    else :
        print(10**nb)