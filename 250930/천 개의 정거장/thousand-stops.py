''' '''
A,B,N = map(int, input().split())
graph = [[] for _ in range(1001)]

for line_no in range(N):
    cost, stop_cnt = map(int, input().split())
    stop = list(map(int, input().split()))

    for i in range(stop_cnt-1):
        graph[stop[i]].append((stop[i+1], cost, line_no))

import heapq

def dijkstra(start):
    costs = [float('inf')] * (1001)
    costs[start] = 0
    # print(cost)
    time = [-1] * (1001)
    time[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    now_line_no = -1

    while q:
        now_cost, now_stop= heapq.heappop(q)

        if now_cost != costs[now_stop]:
            continue

        for next_stop, cost, next_line_no in graph[now_stop]:
            if now_line_no != next_line_no:
                next_cost = now_cost + cost
            else:
                next_cost = now_cost
            if next_cost < costs[next_stop]:
                costs[next_stop] = next_cost
                time[next_stop] = time[now_stop] + 1
                heapq.heappush(q, (next_cost, next_stop))
                now_line_no = next_line_no
    return costs, time

cost, time = dijkstra(A)
if cost[B] == float('inf'):
    print(-1, -1)
else:
    print(cost[B], time[B])

        
