''' A -> 사용된 모든 선분의 c값 중 최소 
B -> 모든 선분의 L값
 B + X / A가 최소'''
import heapq
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)] 
c_list = []
for _ in range(m):
    s, e, l, c = map(int, input().split())
    graph[s].append((e,l,c))
    graph[e].append((s,l,c))
    c_list.append(c)

def get_dist(a,b):
    return b + x / a

def dijkstra(c_limit):
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    a = float('inf')
    q = [(0, 1)] # dist, node

    while q:
        now_d, now_node = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue

        for next_node, l, c in graph[now_node]:
            if c < c_limit:
                continue
            next_d = now_d + l
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node))
    
    return dist

ans = float('inf')
for c_limit in c_list:
    dist = dijkstra(c_limit)
    ans = min(ans, dist[n] + x/c_limit)

print(int(ans))


        
        


        