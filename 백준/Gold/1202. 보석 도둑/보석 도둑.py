n,k = map(int, input().split())
import heapq

present = []

for _ in range(n):
    w, v = map(int, input().split())
    present.append((w,v))
present.sort(key = lambda x: x[0])

backpack = [int(input()) for _ in range(k)]
backpack.sort()

q = []
ans = 0
i = 0
# print(present)
for weight in backpack:
    while i<n and present[i][0] <= weight:
        heapq.heappush(q, -present[i][1])
        i += 1

    if q:
        ans += -heapq.heappop(q)

print(ans)