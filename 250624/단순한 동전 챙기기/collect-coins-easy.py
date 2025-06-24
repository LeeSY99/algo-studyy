n = int(input())

grid = [list(input())  for _ in range(n)]

coin_in_grid = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            si, sj = i, j
        elif grid[i][j] == 'E':
            ei, ej = i, j
        else:
            if grid[i][j] != '.':
                coin_in_grid.append(grid[i][j])

max_len = len(coin_in_grid)
if max_len < 3:
    print(-1)
    exit()

coin_in_grid.sort()
selected_coin = []

def choose(index, count):
    if index == max_len:
        if count == 3:
            calc()
        return

    selected_coin.append(coin_in_grid[index])
    choose(index+1, count+1)
    selected_coin.pop()

    choose(index+1, count)

import sys
ans = sys.maxsize
def calc():
    global ans
    coin_i, coin_j = [0,0,0], [0,0,0]
    first_coin = selected_coin[0]
    second_coin = selected_coin[1]
    third_coin = selected_coin[2]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == first_coin:
                coin_i[0], coin_j[0] = i, j
            elif grid[i][j] == second_coin:
                coin_i[1], coin_j[1] = i, j
            elif grid[i][j] == third_coin:
                coin_i[2], coin_j[2] = i, j
    distance1 = abs(si-coin_i[0]) + abs(sj-coin_j[0])
    distance2 = abs(coin_i[0]-coin_i[1]) + abs(coin_j[0]-coin_j[1])
    distance3 = abs(coin_i[1]-coin_i[2]) + abs(coin_j[1]-coin_j[2])
    distance4 = abs(coin_i[2]-ei) + abs(coin_j[2]-ej)
    ans = min(ans, distance1 + distance2 + distance3 + distance4)

choose(0,0)
print(ans)
        