n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def flip(r,c):
    for i in range(r+1):
        for j in range(c+1):
            gird[i][j] ^= 1

cnt = 0
print(grid)
# for i in range(n-1,-1,-1):
#     for j in range(n-1,-1,-1):
#         if grid[i][j] == 0:
#             flip(i,j)
#             cnt += 1

print(cnt)