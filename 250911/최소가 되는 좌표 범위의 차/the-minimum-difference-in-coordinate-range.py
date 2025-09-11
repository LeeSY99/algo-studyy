from sortedcontainers import SortedSet
n, d = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort()
point_count = SortedSet()

def get_min():
    if not point_count: return 0
    return point_count[0][0]

def get_max():
    if not point_count: return 0
    return point_count[-1][0]

# j = 1
j = 0
ans = float('inf')
for i in range(n):
    while j<n and get_max() - get_min() < d:
        point_count.add((points[j][1], points[j][0]))
        j+=1

    if get_max() - get_min() < d:
        break

    ans = min(ans, points[j-1][0] - points[i][0])

    point_count.remove((points[i][1], points[i][0]))

if ans == float('inf'):
    ans = -1    

print(ans)
        