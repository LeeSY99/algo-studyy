n, d = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(lambda x: (x[1],x[0]))

j = 1
i=0
ans = float('inf')
# print(points)
while j<n:
    y1 = points[i][1]
    y2 = points[j][1]

    if abs(y2-y1) >= d:
        ans = min(ans, abs(points[j][0] - points[i][0]))
        j+=1
    else:
        i+=1
        j=i+1
    
if ans == float('inf'):
    ans = -1    

print(ans)
        