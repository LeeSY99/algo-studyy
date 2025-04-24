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

def tail_move(i,j,er,ec):
    d = directions[i][0]
    if d == 'R':
        grid[er][ec] = 0
        er,ec = er,ec+1
    elif d == 'D':
        grid[er][ec] = 0
        er,ec = er+1,ec
    elif d == 'L':
        grid[er][ec] = 0
        er,ec = er,ec-1
    elif d == 'U':
        grid[er][ec] = 0
        er,ec = er-1,ec
    return er,ec

def solve():
    grid[0][0]=1
    sr, sc = 0,0
    er, ec = 0,0
    time = 0
    taili = 0
    tailp = 0
    for d, p in directions:
        for i in range(p):
            time+=1
            if d == 'R':
                sr,sc = sr,sc+1
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] != 2:
                    er,ec = tail_move(taili,tailp,er,ec)
                    tailp+=1
                    if tailp == directions[taili][1]:
                        taili += 1
                        tailp = 0
                    if grid[sr][sc] == 0:
                        grid[sr][sc] = 1
                    else: return time
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
            elif d == 'D':
                sr,sc = sr+1,sc
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] != 2:
                    er,ec = tail_move(taili,tailp,er,ec)
                    tailp+=1
                    if tailp == directions[taili][1]:
                        taili += 1
                        tailp = 0
                    if grid[sr][sc] == 0:
                        grid[sr][sc] = 1
                    else: return time
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
            elif d == 'L':
                sr,sc = sr,sc-1
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] != 2:
                    er,ec = tail_move(taili,tailp,er,ec)
                    tailp+=1
                    if tailp == directions[taili][1]:
                        taili += 1
                        tailp = 0
                    if grid[sr][sc] == 0:
                        grid[sr][sc] = 1
                    else: return time
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
            elif d == 'U':
                sr,sc = sr-1,sc
                if not in_range(sr,sc):
                    return time
                if grid[sr][sc] != 2:
                    er,ec = tail_move(taili,tailp,er,ec)
                    tailp+=1
                    if tailp == directions[taili][1]:
                        taili += 1
                        tailp = 0
                    if grid[sr][sc] == 0:
                        grid[sr][sc] = 1
                    else: return time
                elif grid[sr][sc] == 2:
                    grid[sr][sc] = 1
    return time

print(solve())        

    

