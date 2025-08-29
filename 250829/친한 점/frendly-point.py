n,m = map(int, input().split())

from sortedcontainers import SortedSet

ss = SortedSet()

for _ in range(n):
    x,y = map(int, input().split())
    ss.add((x,y))

for _ in range(m):
    x,y = map(int, input().split())
    idx = ss.bisect_right((x,y))
    if idx == n:
        print(-1,-1)
    else:
        print(ss[idx][0], ss[idx][1])
