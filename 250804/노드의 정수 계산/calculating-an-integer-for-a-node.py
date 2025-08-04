n = int(input())
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

graph = defaultdict(list)
node = defaultdict()
node[1] = 0

for i in range(2,n+1):
    t,a,p = map(int, input().split())
    if t == 1:
        node[i] = a
    elif t==0:
        node[i] = -a

    # graph[i].append(p)
    graph[p].append(i)

dp = [0] * (n+1)

def dfs(node_num):
    if len(graph[node_num]) == 0:
        # if node[node_num]>0:
        #     dp[node_num] += node[node_num]
        return

    for child_node_num in graph[node_num]:
        dfs(child_node_num)

    for child_node_num in graph[node_num]:
        if node[child_node_num] > 0:
            node[node_num] += node[child_node_num]
        

# print(graph)
# print(node) 
dfs(1)
print(node[1])
