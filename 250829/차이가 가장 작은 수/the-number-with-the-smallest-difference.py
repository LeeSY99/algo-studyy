n,m = map(int, input().split())
from sortedcontainers import SortedSet


arr = [int(input()) for _ in range(n)]
ss = SortedSet(arr)

ans = float('inf')
for num in arr:
    idx2 = ss.bisect_left(num+m)
    idx1 = ss.bisect_right(num-m) - 1

    if idx1 >= 0:
        ans = min(ans, num - ss[idx1])
    
    if idx2 != len(ss):
        ans = min(ans, ss[idx2] - num)


if ans == float('inf'):
    print(-1)
else:
    print(ans)