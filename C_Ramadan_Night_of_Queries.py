
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [max(a[i], b[i]) for i in range(n)]
    
    for i in range(n - 2, -1, -1):
        c[i]=max(c[i], c[i + 1])
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] = p[i] + c[i]
    out = []
    for _ in range(q):
        l, r = map(int, input().split())
        out.append(p[r] - p[l - 1])

    print(' '.join(map(str, out)))