import heapq
n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    nums[i] = -nums[i]

heapq.heapify(nums)

while len(nums) >=2:
    a = -heapq.heappop(nums)
    b = -heapq.heappop(nums)
    if a==b: continue
    heapq.heappush(nums, -(a-b))

if nums:
    print(-nums[0])
else:
    print(-1)
