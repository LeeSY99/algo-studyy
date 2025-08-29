from sortedcontainers import SortedSet

ss = SortedSet([0])
n = int(input())
nums = list(map(int, input().split()))

for num in nums:
    ss.add(num)
    dist = float('inf')
    for i in range(len(ss)-1):
        num1 = ss[i]
        num2 = ss[ss.bisect_right(num1)]
        dist = min(dist, num2-num1)
    print(dist)

