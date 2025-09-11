n, d = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort()

j = n-1
i=0
ans = -1
while i<j:
    y1 = points[i][1]
    y2 = points[j][1]

    if abs(y2-y1) >= d:
        ans = points[j][0] - points[i][0]
        j-=1
    else:
        i+=1

print(ans)
        