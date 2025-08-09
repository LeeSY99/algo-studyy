import heapq
n = int(input())

q = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if not q:
            print(0)
        else:
            abs_x, x = heapq.heappop(q)
            print(x)