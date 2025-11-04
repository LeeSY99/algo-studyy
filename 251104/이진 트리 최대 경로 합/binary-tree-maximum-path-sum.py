n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dp = [0] * (n + 1)
nums = [0]
for i in range(1, n+1):
    num = int(input())
    nums.append(num)

def dfs(x):
    global ans
    visited[x] = True
    child = []
    for y in graph[x]:
        if visited[y] : continue
        dfs(y)
        child.append(y)
    left = child[0] if len(child) >0 else 0
    right = child[1] if len(child )>1 else 0

    dp[x] =  nums[x] + max(0, dp[left], dp[right])
    ans = max(ans, nums[x] + max(0, dp[left]) + max(0, dp[right]))  

visited = [False] * (n+1)
ans = float('-inf')
dfs(1)
print(ans)













# 'ans = float('-inf')
# def get_path(root):
#     global ans
#     if root == None:
#         return 0

#     left_path = get_path(root.left)
#     right_path = get_path(root.right)

#     one_part_max = max(root.num + left_path, root.num + right_path)
#     two_part_max = root.num + left_path + right_path
#     ans = max(ans, one_part_max, two_part_max)

#     return max(one_part_max, 0)
# # print(nodes)
# get_path(nodes[1])
# print(ans)'


