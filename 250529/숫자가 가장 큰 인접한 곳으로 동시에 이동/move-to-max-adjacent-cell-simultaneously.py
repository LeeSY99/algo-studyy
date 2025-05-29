n, m, t = map(int, input().split())

# Create n x n grid
grid = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]


# Please write your code here.
def in_range(r,c):
    return 0<=r<n and 0<=c<n

dr,dc = [-1,1,0,0],[0,0,-1,1]

for i in range(t):
    count = [[0]*n for _ in range(n)]
    for j in range(len(r)):
        r1 = r[j]
        c1 = c[j]
        max_num = 0
        max_index = (0,0)
        for k in range(4):
            next_r, next_c = r1+dr[k], c1+dc[k]
            if in_range(next_r, next_c) and grid[next_r][next_c]>max_num:
                max_num =  grid[next_r][next_c]
                max_index = (next_r,next_c)
        count[max_index[0]][max_index[1]] +=1
    r = []
    c = []
    for a in range(n):
        for b in range(n):
            if count[a][b] ==1:
                r.append(a)
                c.append(b)

# print(r,c)
print(len(r))               
