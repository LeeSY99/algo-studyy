n = int(input())

segs = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for idx, (a, b) in enumerate(segs):
    points.append((a, 1, idx))
    points.append((b, -1, idx))

points.sort()
L = []
R = []

seg_count = 0
ans = 0
for i in range(n):
    lenth = 0
    for x, v, idx in points:
        if idx == i:
            continue
        if seg_count == 0:
            start = x
        seg_count += v
        if seg_count == 0:
            lenth += x-start
    
    ans = max(ans, lenth)

print(ans)
