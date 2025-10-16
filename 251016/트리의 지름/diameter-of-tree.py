n = int(input())
import sys
sys.setrecursionlimit(10000)

edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    edges[a].append((b,c))
    edges[b].append((a,c))

longest = 0
longest_node = None
dist = 0
visited = [False] * (n+1)
def travel(x):
    global dist, longest, longest_node
    for y,d in edges[x]:
        if not visited[y]:
            dist += d
            visited[y] = True
            if dist > longest:
                longest = dist
                longest_node = y
            travel(y)
            dist -= d
visited[1] = True
travel(1)
ans = 0
dist = 0
visited = [False] * (n+1)
# print(longest, longest_node)
def calc(x):
    global dist, ans
    for y,d in edges[x]:
        if not visited[y]:
            dist += d
            visited[y] = True
            # print(x,y,dist)
            ans = max(ans, dist)
            calc(y)
            dist -= d
visited[longest_node] = True
calc(longest_node)
print(ans)