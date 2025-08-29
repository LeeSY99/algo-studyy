n,k = map(int, input().split())

from sortedcontainers import SortedSet

nums = list(map(int, input().split()))
ss = SortedSet(nums)

for i in range(k):
    print(ss[-1-i], end = ' ')