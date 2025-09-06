n = int(input())

segs = [tuple(map(int, input().split()))for _ in range(n)]

points = []
for x1,x2 in segs:
    points.append((x1,1))
    points.append((x2,-1))

points.sort()

max_cnt = 0
cnt = 0
for x, v in points:
    cnt += v
    max_cnt = max(max_cnt, cnt)

print(max_cnt)