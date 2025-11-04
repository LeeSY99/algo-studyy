n = int(input())
node = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#dp[i] : i를 루트로 하는 서브트리를 모두 1로 만들고 난 후의 i값
dp = [0] * (n+1)
ans = 0
def dfs(x):
    global ans
    visited[x] = True
    dp[x] = node[x]
    for y in graph[x]:
        if visited[y]: continue      
        dfs(y)
        dp[x] += dp[y]-1
    
    ans += abs(dp[x]-1)

visited = [False] * (n+1)
dfs(1)
print(ans)





