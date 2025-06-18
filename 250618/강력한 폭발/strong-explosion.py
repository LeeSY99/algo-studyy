n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(i,j):
    return 0<= i <n and 0<= j <n

def bomb1(i,j,after_boom):
    # global after_boom
    for k in range(3):
        if in_range(i-k,j):
            after_boom[i-k][j] = 1
        if in_range(i+k,j):
            after_boom[i+k][j] = 1

def bomb2(i,j,after_boom):
    # global after_boom
    for k in range(2):
        if in_range(i-k,j):
            after_boom[i-k][j] = 1
        if in_range(i,j+k):
            after_boom[i][j+k] = 1
        if in_range(i+k,j):
            after_boom[i+k][j] = 1
        if in_range(i,j-k):
            after_boom[i][j-k] = 1

def bomb3(i,j,after_boom):
    # global after_boom
    for k in range(2):
        if in_range(i-k,j-k):
            after_boom[i-k][j-k] = 1
        if in_range(i-k,j+k):
            after_boom[i-k][j+k] = 1
        if in_range(i+k,j+k):
            after_boom[i+k][j+k] = 1
        if in_range(i+k,j-k):
            after_boom[i+k][j-k] = 1

bomb_count=0
bomb_index = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            bomb_count+=1
            bomb_index.append((i,j))

bomb = []

def bomb_insert(count):
    if count == bomb_count:
        after_boom = [[0]*n for _ in range(n)]
        boom(after_boom)
        return

    for i in range(1,4):
        bomb.append(i)
        bomb_insert(count + 1)
        bomb.pop()


ans = 0
def boom(after_boom):
    global ans
    for index in range(len(bomb_index)):
        i, j = bomb_index[index]
        if bomb[index] == 1:
            bomb1(i,j,after_boom)
        elif bomb[index] == 2:
            bomb2(i,j,after_boom)
        else:
            bomb3(i,j,after_boom)
    count = 0
    for i in range(n):
        for j in range(n):
            if after_boom[i][j] == 1:
                count+=1
    ans = max(ans, count)

bomb_insert(0)
print(ans)
# print(asdf)
    
    