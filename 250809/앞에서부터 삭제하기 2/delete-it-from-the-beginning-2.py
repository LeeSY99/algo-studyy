n = int(input())
nums = list(map(int, input().split()))
import heapq


ans = 0
num_sum = 0
q = []

heapq.heappush(q,nums[n-1])
num_sum += nums[n-1]

for k in range(n-2,0,-1):
    heapq.heappush(q, nums[k])
    num_sum += nums[k]

    avg = (num_sum - q[0]) / (len(q)-1)

    ans = max(ans,avg)

print(f"{ans:.2f}")


