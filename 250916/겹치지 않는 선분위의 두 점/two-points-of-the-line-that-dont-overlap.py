n,m = map(int, input().split())

points = []

for _ in range(m):
    a, b = map(int, input().split())
    points.append((a,b))

left = 0
right = 10**18
ans = 0

points.sort()

def check(dist):
    count = 0
    start = -1
    for i in range(m):
        a, b = points[i]
        if a > start:
            count += 1
            start = a + dist
        while start <= b:
            count += 1
            start = start + dist
    # print(dist, count)
    return count >= n


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)

