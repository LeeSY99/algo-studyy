n, k = map(int, input().split())

points = []
for _ in range(n):
    p = int(input())
    points.append(p)

points.sort()

left = 1
right = 10**9
ans = 10**9

def check(r):
    count = 0
    start = float('-inf')
    for x in points:
        if x - r > start + r:
            count += 1
            start = x
    
    return count <= k
            

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)
    