'''n*n격자
동전 있으면 1 없으면 0
3*3격자를 벗어나지 않게 하면서 격자 안의 동전을 최대로'''
n = int(input())

grid = [list(map(int, input().split()))  for _ in range(n)]


def check(i,j):
    coins = 0
    for r in range(i,i+3):
        for c in range(j,j+3):
            if grid[r][c]: coins+=1
    return coins


ans = 0
for i in range(n-2):
    for j in range(n-2):
        ans = max(ans,check(i,j))

print(ans)



