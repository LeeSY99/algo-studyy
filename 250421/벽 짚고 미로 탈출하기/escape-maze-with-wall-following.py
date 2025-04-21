N = int(input())
x, y = map(int, input().split())

grid = [["."] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    row = input()
    for j in range(1, N + 1):
        grid[i][j] = row[j - 1]

# Please write your code here.

dx, dy = [1,0,-1,0], [0,-1,0,1]

def in_range(r,c):
    return 0<=r<N and 0<=c<N

def solve():
    global x,y
    time = 0
    i = 0
    x ,y = x-1, y-1
    while 1:
        time+=1
        grid[x][y]=0
        while 1:
            count = 0
            if in_range(x+dx[i], y+dy[i]):
                if grid[x+dx[i]][y+dy[i]] == '#':
                    count+=1
                    i = (i+1) % 4
                    if count>=4:
                        return -1
                elif grid[x+dx[i]][y+dy[i]] == '.':
                    x = x+dx[i]
                    y = y+dy[i]
                    break
                elif grid[x+dx[i]][y+dy[i]] == '0':
                    return -1
            else:
                return time

print(solve())
    
