n = int(input())
nums = list(map(int, input().split()))
import heapq
heapq.heapify(nums)

count = 0

for _ in range(n-1):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    count += (a+b)
    heapq.heappush(nums, a+b)

print(count)
