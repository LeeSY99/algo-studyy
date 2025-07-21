n = int(input())
import heapq
nums = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(nums, x)
    elif x == 0:
        if len(nums) == 0:
            print(0)
        else:
            print(heapq.heappop(nums))
        
