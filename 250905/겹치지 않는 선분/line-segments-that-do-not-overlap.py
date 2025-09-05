n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

points.sort()
# print(points)

L = [0] * n
R = [0] * n

for i in range(n):
    if i == 0:
        L[i] = 1
    else:
        if points[i][0] >= points[i-1][1] or points[i][1] > points[i-1][1]:
            L[i] = L[i-1] + 1
        else:
            L[i] = L[i-1]

for i in range(n-1,-1,-1):
    if i == n-1:
        R[i] = 1

    else:
        if points[i][1] <= points[i+1][0] or points[i][1] < points[i+1][1]:
            R[i] = R[i+1] + 1
        else:
            R[i] = R[i+1]

print((R[0] + L[0])//2)