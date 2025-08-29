n,m = map(int, input().split())

from sortedcontainers import SortedSet

ss = SortedSet()
for _ in range(n):
    x,y = map(int, input().split())
    ss.add((x,y))

for _ in range(m):
    k = int(input())
    idx = ss.bisect_left((k,0))
    if idx == len(ss):
        print(-1,-1)
    else:
        print(ss[idx][0], ss[idx][1])
        ss.remove((ss[idx][0], ss[idx][1]))