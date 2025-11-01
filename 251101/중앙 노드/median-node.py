n,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)
cent = r
def dfs(x):
    global cent
    visited[x] = True
    c_cnt = 0
    cent = x
    for y in graph[x]:
        if not visited[y]:
            parent[y] = x
            visited[y] = True
            c_cnt+=1
            dfs(y)
    if c_cnt > 1:
        cent = x
        
visited = [False] * (n+1)
dfs(r)
# print('root', r)
# print('cent_node:', cent)

size = [0] * (n+1)
def get_ans(x, p):
    size[x] = 1
    for y in graph[x]:
        if y == p:
            continue
        get_ans(y,x)
        size[x] += size[y]

get_ans(cent,parent[cent])

max_size = 0
min_size = 100000
cent_sub = [size[v] for v in graph[cent] if v != parent[cent]]
# print(cent_sub)
if not cent_sub:
    print(0)
else:
    print(max(cent_sub) - min(cent_sub))

    