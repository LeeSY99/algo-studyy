n = int(input())
can_go = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    can_go[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if can_go[i][k] and can_go[k][j]:
                can_go[i][j] = 1

for graph in can_go:
    print(*graph)