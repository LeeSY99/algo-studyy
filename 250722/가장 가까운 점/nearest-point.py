n,m = map(int, input().split())

import heapq
points = []

for _ in range(n):
    x,y = map(int, input().split())
    heapq.heappush(points,(x+y,x,y))

for _ in range(m):
    closest = heapq.heappop(points)
    cx, cy = closest[1], closest[2]
    cx+=2
    cy+=2
    heapq.heappush(points,(cx+cy,cx,cy))

closest = heapq.heappop(points)
print(closest[1], closest[2])
