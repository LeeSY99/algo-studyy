n,m,k = map(int, input().split())

grid = [[0]*n for _ in range(n)]
for _ in range(m):
    r,c = map(int, input().split())
    grid[r-1][c-1] = 2

directions = []
for _ in range(k):
    d,p = input().split()
    directions.append((d,int(p)))

# Please write your code here.
def in_range(r,c):
    return 0<=r<n and 0<=c<n

def solve():
    grid[0][0]=1
    sr, sc = 0,0
    er, ec = 0,0
    time = 0
    for d, p in directions:
        for i in range(p):
            time+=1
            if d == 'R':
                sr,sc = sr,sc+1
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] == 0:
                    grid[sr][sc] = 1
                    grid[er][ec] = 0
                    er,ec = er,ec+1
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
                elif grid[sr][sc] == 1:
                    return time
            elif d == 'D':
                sr,sc = sr+1,sc
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] == 0:
                    grid[sr][sc] = 1
                    grid[er][ec] = 0
                    er,ec = er+1,ec
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
                elif grid[sr][sc] == 1:
                    return time
            elif d == 'L':
                sr,sc = sr,sc-1
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] == 0:
                    grid[sr][sc] = 1
                    grid[er][ec] = 0
                    er,ec = er,ec-1
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
                elif grid[sr][sc] == 1:
                    return time
            elif d == 'U':
                sr,sc = sr-1,sc
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] == 0:
                    grid[sr][sc] = 1
                    grid[er][ec] = 0
                    er,ec = er-1,ec
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
                elif grid[sr][sc] == 1:
                    return time
    return time

print(solve())        

    

