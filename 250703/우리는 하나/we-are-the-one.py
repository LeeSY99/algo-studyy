n,k,u,d = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
selected_index = []
ans = 0
def choose(index, count):
    global ans
    if index == n**2:
        if count == k:
            cities = check(selected_index)
            ans = max(ans, cities)
        return
        
    selected_index.append((index//n, index%n))
    choose(index+1,count+1)

    selected_index.pop()
    choose(index+1,count)

def in_range(r,c):
    return 0<=r<n and 0<=c<n

drs, dcs = [-1,1,0,0],[0,0,-1,1]
def check(indexes):
    count = 0
    visited = [[0]*n for _ in range(n)]
    q = deque(indexes)
    while q:
        r, c = q.pop()
        visited[r][c] = 1
        count+=1
        for dr, dc in zip(drs,dcs):
            nr = r+dr
            nc = c+dc
            if in_range(nr,nc):
                if not visited[nr][nc] and u <= abs(city[r][c]-city[nr][nc]) <=d:
                    visited[nr][nc] = 1
                    q.append((nr,nc))
    return count

choose(0,0)
print(ans)
    