''' '''
A,B,N = map(int, input().split())
graph = [[] for _ in range(1001)]

for line_no in range(1,N+1):
    cost, stop_cnt = map(int, input().split())
    stop = list(map(int, input().split()))

    for i in range(stop_cnt-1):
        graph[stop[i]].append((stop[i+1], cost, line_no))

import heapq
def dijkstra(start):
    costs = [[float('inf')] * (N+1) for _ in range(1001)]
    time = [[float('inf')] * (N+1) for _ in range(1001)]
    costs[start][0] = 0
    time[start][0] = 0
    
    q = [(0, 0, start, 0)] #비용, 시간,  출발, , 노선번호

    while q:
        now_cost, now_time, now_stop, now_line_no = heapq.heappop(q)

        if now_cost != costs[now_stop][now_line_no]:
            continue

        for next_stop, cost, next_line_no in graph[now_stop]:
            if now_line_no != next_line_no:
                next_cost = now_cost + cost
            else:
                next_cost = now_cost

            if next_cost < costs[next_stop][next_line_no] or \
                (next_cost == costs[next_stop][next_line_no] and now_time + 1 < time[next_stop][next_line_no]):
                costs[next_stop][next_line_no] = next_cost
                time[next_stop][next_line_no] = now_time + 1
                heapq.heappush(q, (next_cost, now_time+1, next_stop, next_line_no))
    best_cost = min(costs[B])
    if best_cost == float('inf'):
        return -1,-1
    best_time = min(time[B][j] for j in range(1,N+1) if costs[B][j] == best_cost)
    return best_cost, best_time

ans_cost, ans_time = dijkstra(A)
print(ans_cost, ans_time)

        
