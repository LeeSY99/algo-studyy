n,m = map(int, input().split())
from sortedcontainers import SortedSet

ss1 = SortedSet()
ss2 = SortedSet()

ans = float('inf')
for _ in range(n):
    num = int(input())
    idx2 = ss2.bisect_left(num+m)
    idx1 = ss1.bisect_left(-(num-m))

    if idx1 != len(ss1):
        ans = min(ans, num + ss1[idx1])

    if idx2 != len(ss2):
        ans = min(ans, ss2[idx2] - num)

    ss1.add(-num)
    ss2.add(num)

if ans == float('inf'):
    print(-1)
else:
    print(ans)