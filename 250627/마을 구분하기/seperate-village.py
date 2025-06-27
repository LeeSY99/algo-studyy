n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dis, djs =[1,0,0,-1],[0,1,-1,0]

ans = []

def in_range(i,j):
    return 0<=i<n and 0<=j<n

def check(i,j):
    count = 0
    def dfs(i,j):
        nonlocal count
        count+=1
        visited[i][j] = 1
        if i>=n or j>=n:
            return

        for di, dj in zip(dis, djs):
            ni, nj = i+di, j+dj
            if in_range(ni,nj) and grid[ni][nj] and not visited[ni][nj]:
                dfs(ni,nj)
    dfs(i,j)
    return count


for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            ans.append(check(i,j))

ans.sort()
print(len(ans))
for a in ans:
    print(a)
        


    
