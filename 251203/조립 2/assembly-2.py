from collections import deque
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)

for _ in range(m):
    a,k = map(int, input().split())
    piece = list(map(int, input().split()))
    for i in range(k):
        graph[piece[i]].append(a)
    in_degree[a] += k

now = int(input())
now_piece = list(map(int, input().split()))
for p in now_piece:
    in_degree[p] = 0
q = deque(now_piece)
can = now_piece

while q:
    x = q.popleft()

    for y in graph[x]:
        in_degree[y]-=1
        if in_degree[y] == 0:
            q.append(y)
            can.append(y)

can.sort()
print(len(can))
print(*can)


