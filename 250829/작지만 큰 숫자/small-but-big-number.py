n,m = map(int, input().split())

nums = list(map(int, input().split()))
query = list(map(int, input().split()))

from sortedcontainers import SortedSet
ss= SortedSet(nums)

for q in query:
    idx = ss.bisect_right(q)
    idx -= 1
    if idx < 0:
        print(-1)
    else:
        print(ss[idx])
        ss.remove(ss[idx])
