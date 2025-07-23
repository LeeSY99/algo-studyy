n,m = map(int, input().split())

is_coin = [[0] * n for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    is_coin[r-1][c-1] = 1

for a in is_coin:
    print(*a)