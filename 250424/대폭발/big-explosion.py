n, m, r, c = map(int, input().split())

# Please write your code here.

grid = [[0]*n for _ in range(n)]

def in_range(r,c):
    return 0<=r<n and 0<=c<n

r,c = r-1,c-1
grid[r][c] = 1

for time in range(1, m+1):
    new = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                new[i][j] = 1
                if in_range(i-2**(time-1), j):
                    new[i-2**(time-1)][j] = 1
                if in_range(i, j+2**(time-1)):
                    new[i][j+2**(time-1)] = 1
                if in_range(i+2**(time-1), j):
                    new[i+2**(time-1)][j] = 1
                if in_range(i, j-2**(time-1)):
                    new[i][j-2**(time-1)] = 1
    
    for i in range(n):
        for j in range(n):
            # if grid[i][j] == 1:
            #     continue
            grid[i][j]=new[i][j]

ans=0
for a in grid:
    ans+=sum(a)

print(ans)

