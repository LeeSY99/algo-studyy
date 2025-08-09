n = int(input())
nums = list(map(int, input().split()))
all_p = 1
import heapq
q = []
for i in range(n):
    if i<2:
        print(-1)
        heapq.heappush(q, nums[i])
    else:
        heapq.heappush(q, nums[i])

        a = heapq.heappop(q)
        b = heapq.heappop(q)
        c = heapq.heappop(q)
        print(a*b*c)
        heapq.heappush(q,a)
        heapq.heappush(q,b)
        heapq.heappush(q,c)