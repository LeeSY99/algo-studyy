n = int(input())
seg = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for x1,x2 in seg:
    points.append((x1,1))
    points.append((x2,-1))

points.sort()

max_val = 0
val = 0
for x, v in points:
    val += v
    max_val = max(max_val, val)

print(max_val)


