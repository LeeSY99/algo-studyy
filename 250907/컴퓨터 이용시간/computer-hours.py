n = int(input())
segs = [tuple(map(int, input().split())) for _ in range(n)]
import heapq
points = []

for idx,( p, q) in enumerate(segs, 1):
    points.append((p,1,idx))
    points.append((q,-1,idx))

points.sort()

people = [0] * (n+1)
c_valid = [i for i in range(1,n+1)]

seg_count = 0

for x, v, p_num in points:
    if v == 1:
        people[p_num] = heapq.heappop(c_valid)
    else:
        c_num = people[p_num]
        heapq.heappush(c_valid, c_num)

for i in range(1,n+1):
    print(people[i], end = ' ')
    
    