import heapq
n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[1], x[0]))


now = 0
score = 0
idx = n-1
pq = []

for t in range(10000,0,-1):
    while idx >= 0 and arr[idx][1] >= t:
        heapq.heappush(pq, -arr[idx][0])
        idx -= 1
    
    if pq:
        score += -heapq.heappop(pq)

print(score)