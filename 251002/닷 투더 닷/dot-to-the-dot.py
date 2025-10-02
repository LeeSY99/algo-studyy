''' A -> 사용된 모든 선분의 c값 중 최소 
B -> 모든 선분의 L값
 B + X / A가 최소'''
import heapq
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)] 

for _ in range(m):
    s, e, l, c = map(int, input().split())
    graph[s].append((e,l,c))
    graph[e].append((s,l,c))

def get_dist(a,b):
    return b + x / a

def dijkstra():
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    a = float('inf')
    q = [(0, 1, float('inf'), 0)] # dist, node, A, B

    while q:
        now_d, now_node, a, b = heapq.heappop(q)

        if now_d != dist[now_node]:
            continue

        for next_node, l, c in graph[now_node]:
            new_b = b + l
            new_a = min(a, c)
            # print(now_node, new_a, new_b)
            next_d = get_dist(new_a,new_b)
            if next_d < dist[next_node]:
                dist[next_node] = next_d
                heapq.heappush(q, (next_d, next_node, new_a, new_b))
    return dist[n]
    # return dist

print(dijkstra())


        
        


        