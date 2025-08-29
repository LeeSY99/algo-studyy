n,m = map(int, input().split())

from sortedcontainers import SortedSet
nums = list(map(int, input().split()))
ss = SortedSet(nums)

for _ in range(m):
    num = int(input())
    idx = ss.bisect_left(num)
    if idx == n:
        print(-1)
    else:
        print(ss[idx])
