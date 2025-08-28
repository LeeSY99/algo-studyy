n = int(input())

points = {}

for _ in range(n):
    x,y = map(int, input().split())
    if x in points:
        if y < points[x]:
            points[x] = y
    else:
        points[x] = y


ans = 0
for x,y in points.items():
    ans += y

print(ans)