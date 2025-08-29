from sortedcontainers import SortedSet

ss = SortedSet([0])
n = int(input())
nums = list(map(int, input().split()))

dist = float('inf')
for num in nums:
    ss.add(num)
    
    idx1 = ss.bisect_left(num) - 1
    idx2 = ss.bisect_right(num)
    if idx2 == len(ss):
        dist = min(dist, num-ss[idx1])
    else:
        dist = min(dist, num-ss[idx1], ss[idx2]-num)
    print(dist)
        

