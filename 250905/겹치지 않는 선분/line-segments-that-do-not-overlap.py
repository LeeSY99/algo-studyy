n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()
# print(points)

L = [0] * n
R = [0] * n

for i in range(n):
    x1, x2 = points[i]
    if i == 0:
        L[i] = x2
    else:
        L[i] = max(L[i-1], x2)

for i in range(n-1,-1,-1):
    x1, x2 = points[i]
    if i == n-1:
        R[i] = x2

    else:
        R[i] = min(R[i+1],x2)


ans = 0
for i in range(n):
    x1,x2 = points[i]
    if i>0 and L[i-1] >= x2:
        continue

    if i<n-1 and R[i+1] <= x2:
        continue
    
    ans +=1
print(ans)