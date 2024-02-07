def count_less_or_equal(a, b):
    counts = [0] * len(b)
    a.sort()
 
    for i, bi in enumerate(b):
        count = 0
        left, right = 0, len(a)
 
        while left < right:
            mid = (left + right) // 2
            if a[mid] <= bi:
                count = mid + 1
                left = mid + 1
            else:
                right = mid
 
        counts[i] = count
 
    return counts
 
# Read input
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
 
# Calculate and print the result
result = count_less_or_equal(a, b)
print(*result)
