n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

from collections import deque
q = deque()
q.append((0,0))
visited[0][0] = 1

def in_range(i,j):
    return 0<=i<n and 0<=j<m

dis, djs = [0,1,0,-1], [1,0,-1,0]

def bfs():
    while q:
        cur_i, cur_j = q.popleft()
        if cur_i == n-1 and cur_j == m-1:
            return True
        for di, dj in zip(dis, djs):
            n_i, n_j = cur_i+di, cur_j+dj
            if in_range(n_i, n_j) and grid[n_i][n_j] and not visited[n_i][n_j]:
                visited[n_i][n_j] = 1
                q.append((n_i, n_j))
    return False

print(int(bfs()))






