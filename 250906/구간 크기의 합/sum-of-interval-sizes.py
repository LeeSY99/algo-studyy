n = int(input())

segs = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for x1, x2 in segs:
    points.append((x1,1))
    points.append((x2,-1))

points.sort()

val = 0
ans = 0
for x, v in points:
    if val == 0:
        start = x
    val += v
    if val == 0:
        ans+= x-start

print(ans)

