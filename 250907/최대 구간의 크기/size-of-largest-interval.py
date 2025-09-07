n = int(input())
segs = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for a, b in segs:
    points.append((a,1))
    points.append((b,-1))

points.sort()

seg_count = 0
ans = 0

for x, v in points:
    if seg_count == 0:
        start = x

    seg_count += v

    if seg_count == 0:
        ans = max(ans, x-start)

print(ans)