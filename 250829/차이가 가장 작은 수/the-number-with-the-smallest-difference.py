n,m = map(int, input().split())
from sortedcontainers import SortedSet

ss = SortedSet()

ans = float('inf')
for _ in range(n):
    num = int(input())
    idx2 = ss.bisect_left(num+m)
    idx1 = ss.bisect_right((num-m)) - 1

    if idx1 >= 0:
        ans = min(ans, num - ss[idx1])
    
    if idx2 != len(ss):
        ans = min(ans, ss[idx2] - num)

    ss.add(num)

if ans == float('inf'):
    print(-1)
else:
    print(ans)