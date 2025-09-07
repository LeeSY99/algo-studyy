from sortedcontainers import SortedSet
n = int(input())

segs = [tuple(map(int, input().split())) for _ in range(n)]

points = []
for i,(y,x1,x2) in enumerate(segs):
    points.append((x1,1,i,y))
    points.append((x2,-1,i,y))

points.sort()
visible = [False] * n

segs = SortedSet()

for x, v, idx, y in points:
    if v == 1:
        segs.add((y,idx))
    else:
        segs.remove((y, idx))
    
    if not segs:
        continue

    _, target_index = segs[0]
    visible[target_index] =True
    
print(sum(visible))

    
    
