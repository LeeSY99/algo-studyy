n = int(input())

nums = [0] + list(map(int, input().split()))
import sys
sys.setrecursionlimit(10**6)


edges = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

# i번 노드 색칠 x dp[i][0]
# i번 노드 색칠 o dp[i][1]
dp = [[0,0] for _ in range(n+1)]  
# print(dp)

def dfs(x):
    dp[x][1] = nums[x]

    for y in edges[x]:
        if visited[y]:
            continue
        visited[y] = 1
        dfs(y)

        #x노드가 선택하면 근처노드는 선택할 수 없음
        dp[x][1] += dp[y][0]
        #x노드가 선택하지 않으면 근처노드는 포함될수도 있고 안될수도
        dp[x][0] += max(dp[y][0], dp[y][1])


visited[1] = 1
dfs(1)

print(max(dp[1][0], dp[1][1]))

