n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

FULL = (1<<n) - 1
dp = [[-1] * (1<<n) for _ in range(n)]
def tsp(cur, mask):
    if mask == FULL:
        return (arr[cur][0] if arr[cur][0] != 0 else float('inf'))

    if dp[cur][mask] != -1:
        return dp[cur][mask]

    best = float('inf')
    for next in range(n):
        if mask & (1<<next):
            continue
        if arr[cur][next] == 0:
            continue
        cand = arr[cur][next] + tsp(next, mask | (1<<next))
        if cand < best:
            best=cand
            
    dp[cur][mask] = best
    return best

print(tsp(0,1<<0))