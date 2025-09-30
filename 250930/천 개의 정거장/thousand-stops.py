''' '''
A,B,N = map(int, input().split())
INF = float('inf')
graph = [[(INF, 0)] * (1001) for _ in range(1001)]
dist = [(INF, 0)] * 1001
visited = [False] * 1001

for i in range(1, 1001):
    graph[i][i] = (0,0)

for _ in range(N):
    cost, stop_num = map(int, input().split())
    stops = list(map(int, input().split()))

    for i in range(stop_num):
        for j in range(i+1, stop_num):
            graph[stops[i]][stops[j]] = min(graph[stops[i]][stops[j]], (cost, j-i))

dist[A] = (0,0)
for _ in range(1000):
    min_index = -1
    for i in range(1,1001):
        if visited[i]: continue

        if min_index == -1 or dist[min_index] >  dist[i]:
            min_index = i
    visited[min_index] = True
    min_cost, min_time = dist[min_index]

    for i in range(1, 1001):
        cost, time = graph[min_index][i]
        dist[i] = min(dist[i], (min_cost+cost, min_time + time))

if dist[B] == (INF, 0):
    dist[B] = (-1, -1)

min_cost, min_time = dist[B]
print(min_cost, min_time)  

# for line_no in range(1,N+1):
#     cost, stop_cnt = map(int, input().split())
#     stop = list(map(int, input().split()))

#     for i in range(stop_cnt-1):
#         graph[stop[i]].append((stop[i+1], cost, line_no))

# import heapq
# def dijkstra(start):
#     costs = [[float('inf')] * (N+1) for _ in range(1001)]
#     time = [[float('inf')] * (N+1) for _ in range(1001)]
#     costs[start][0] = 0
#     time[start][0] = 0
    
#     q = [(0, 0, start, 0)] #비용, 시간,  출발, , 노선번호

#     while q:
#         now_cost, now_time, now_stop, now_line_no = heapq.heappop(q)

#         if now_cost != costs[now_stop][now_line_no]:
#             continue

#         for next_stop, cost, next_line_no in graph[now_stop]:
#             if now_line_no != next_line_no:
#                 next_cost = now_cost + cost
#             else:
#                 next_cost = now_cost

#             if next_cost < costs[next_stop][next_line_no] or \
#                 (next_cost == costs[next_stop][next_line_no] and now_time + 1 < time[next_stop][next_line_no]):
#                 costs[next_stop][next_line_no] = next_cost
#                 time[next_stop][next_line_no] = now_time + 1
#                 heapq.heappush(q, (next_cost, now_time+1, next_stop, next_line_no))
#     best_cost = min(costs[B])
#     if best_cost == float('inf'):
#         return -1,-1
#     best_time = min(time[B][j] for j in range(1,N+1) if costs[B][j] == best_cost)
#     return best_cost, best_time

# ans_cost, ans_time = dijkstra(A)
# print(ans_cost, ans_time)

        
