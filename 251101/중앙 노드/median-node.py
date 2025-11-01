import sys
sys.setrecursionlimit(1000000)
n,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n+1)
size = [0]*(n+1)
best_cent, best_val = 1, n

def find_cent(x, p):
    global best_cent, best_val
    size[x] = 1
    max_child = 0
    for y in graph[x]:
        if y == p:
            continue
        find_cent(y,x)
        size[x] += size[y]
        if size[y] > max_child:
            max_child = size[y]
    comp_biggest = max(max_child, n-size[x])
    if comp_biggest <  best_val:
        best_val = comp_biggest
        best_cent = x
       
find_cent(r,0)
cent = best_cent
# print('root', r)
# print('cent_node:', cent)

size2 = [0] * (n+1)
def get_ans(x, p):
    size2[x] = 1
    for y in graph[x]:
        if y == p:
            continue
        get_ans(y,x)
        size2[x] += size2[y]

get_ans(cent,parent[cent])

max_size = 0
min_size = 100000
cent_sub = [size2[v] for v in graph[cent] if v != parent[cent]]
# print(cent_sub)
if not cent_sub:
    print(0)
else:
    print(max(cent_sub) - min(cent_sub))

    