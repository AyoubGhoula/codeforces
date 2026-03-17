# from collections import deque


# # t=[]



# # Q=deque(t)


# # Q.append(1)
# # Q.popleft()








# t=[]

# Q=deque(t)

# for _ in range(int(input())):
#     nb=0
#     ch=""
#     for i in range(int(input())):
#         nb+=1
#         a,b=map(int,input().split())
#         if not t:
#             ch=" "+str(nb)
#             nb+=1
#         else:
#             Q.append((a,b))
        
#         if Q:
#             while Q:
#                 if Q[0][0]-Q[0][1]<=nb:
#                     Q.popleft()
#                     ch+=" "+str(nb)
#                     nb+=1
#                 else:
#                     break
#         print(ch[1::])



# # ch=input()
# # t=[]
# # ruselt=0
# # for i in ch:
# #     if i == "(":
# #         t.append(i)
# #     elif i == ")":
# #         if t and t[-1] == "(":
# #             t.pop()
# #             ruselt+=2
# #         else:
# #             t.append(i)
# # print(ruselt)




# # for _ in range(int(input())):
# #     n=int(input())
# #     if n<=10:
# #         print(0)
# #     else:
# #         print(10)








# for _ in range(int(input())):
#     n=int(input())
#     a=input()
#     m=int(input())
#     b=input()
#     c=input()
#     for i in range(m): 
#         if c[i]=="V":
#             a=b[i]+a
#         elif c[i]=="D":
#             a=a+b[i]
#     print(a)



# for _ in range(int(input())):
#     n=int(input())
#     a=input()
#     m=int(input())
#     b=input()
#     c=input()
#     for i in range(m): 
#         if c[i]=="V":
#             a=b[i]+a
#         elif c[i]=="D":
#             a=a+b[i]
#     print(a)



# n=int(input())

# b=n//2
# print(b)
# if n%2==0:
#     print("2 "*b)
# else:
#     print("2 "*(b-1)+"3")





    

# t = int(input())
# for _ in range(t):
#     n, q = map(int, input().split())
#     a = list(map(int, input().split()))
#     b = list(map(int, input().split()))
#     c = [max(a[i], b[i]) for i in range(n)]
    
#     for i in range(n - 2, -1, -1):
#         c[i]=max(c[i], c[i + 1])
#     p = [0] * (n + 1)
#     for i in range(n):
#         p[i + 1] = p[i] + c[i]
#     out = []
#     for _ in range(q):
#         l, r = map(int, input().split())
#         out.append(p[r] - p[l - 1])

#     print(' '.join(map(str, out)))




