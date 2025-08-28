n = int(input())
from sortedcontainers import SortedDict

sd = SortedDict()

nums = list(map(int, input().split()))

for i, num in enumerate(nums, 1):
    if num not in sd:
        sd[num] = i

for num , count in sd.items():
    print(num, count)