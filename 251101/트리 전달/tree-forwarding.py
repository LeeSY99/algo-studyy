n,m = map(int, input().split())
parent = [0] + list(map(int, input().split()))
score = [0] * (n+1)
for _ in range(m):
    i,w = map(int, input().split())
    score[i] += score[parent[i]] + w

print(*score[1:])