from sortedcontainers import SortedSet

n,m = map(int, input().split())
ss = SortedSet([i for i in range(1,m+1)])

nums = list(map(int, input().split()))
for num in nums:
    ss.remove(num)
    print(ss[-1])