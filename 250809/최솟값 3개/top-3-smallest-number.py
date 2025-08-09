n = int(input())
nums = list(map(int, input().split()))
all_p = 1
import heapq
q = []
for i in range(n):
    heapq.heappush(q, -nums[i])
    if i<2:
        print(-1)
    else:
        if len(q) > 3:
            heapq.heappop(q)
            
        a,b,c = [-v for v in q]
        print(a*b*c)


    
    

    