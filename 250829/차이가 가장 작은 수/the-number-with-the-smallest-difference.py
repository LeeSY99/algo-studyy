n,m = map(int, input().split())
from sortedcontainers import SortedSet

ss = SortedSet()

ans = float('inf')
for _ in range(n):
    num = int(input())
    idx1 = ss.bisect_right(num)
    idx2 = idx1 - 1

    if idx1 != len(ss):
        if ss[idx1] - ss[idx2] >=m:
            ans = min(ans, ss[idx1] - ss[idx2])
    ss.add(num)

if ans == float('inf'):
    print(-1)
else:
    print(ans)