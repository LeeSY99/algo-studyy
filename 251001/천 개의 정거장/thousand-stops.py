''' '''
A,B,N = map(int, input().split())
INF = float('inf')
graph = [[] * (1001) for _ in range(1001)]

for line_no in range(1,N+1):
    cost, stop_cnt = map(int, input().split())
    stop = list(map(int, input().split()))

    for i in range(stop_cnt):
        for j in range(i+1, stop_cnt):
            u, v = stop[i], stop[j]
            t = j - i
            graph[u].append((v,cost,t))

import heapq
def dijkstra(start):
    dist = [(INF, 0) for _ in range(1001)]
    dist[start] = (0,0)
    
    q = [(0, 0, start)] #비용, 시간,  출발

    while q:
        now_cost, now_time, now_stop = heapq.heappop(q)

        if (now_cost, now_time) != dist[now_stop]:
            continue

        for next_node, next_cost, next_time in graph[now_stop]:
            nxt = (now_cost + next_cost, now_time + next_time)
            if nxt < dist[next_node]:
                dist[next_node] = nxt
                heapq.heappush(q, (nxt[0], nxt[1], next_node))
    return (-1, -1) if dist[B][0] == INF else (dist[B][0], dist[B][1])
            

ans_cost, ans_time = dijkstra(A)
print(ans_cost, ans_time)

        
