n, q = map(int, input().split())

points = list(map(int, input().split()))

from sortedcontainers import SortedSet
nums = SortedSet(points)

mapper = dict()
cnt = 1
for num in nums:
    mapper[num] = cnt
    cnt += 1

for _ in range(q):
    a,b = map(int, input().split())
    print(mapper[b]- mapper[a] + 1) 

