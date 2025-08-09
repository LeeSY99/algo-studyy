n,m,k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

import heapq
q = []


for i in range(n):
    heapq.heappush(q, (arr1[i]+ arr2[0], i, 0))

for i in range(k-1):
    val, idx1, idx2 = heapq.heappop(q)

    idx2 +=1
    if idx2 < m:
        heapq.heappush(q,(arr1[idx1] + arr2[idx2], idx1, idx2))

ans, idx1, idx2 = heapq.heappop(q)
print(ans)

