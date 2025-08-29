n,m = map(int, input().split())
from sortedcontainers import SortedSet

ss = SortedSet([-i for i in range(1,m+1)])

people = list(map(int, input().split()))

count = 0
for p in people:
    idx = ss.bisect_left(-p)
    if idx == len(ss):
        break
    count += 1
    ss.remove(ss[idx])

print(count)