n, k = map(int, input().split())
nodes = list(map(int, input().split()))

root = nodes[0]
parent = [-1] * (n)

parent_node_idx = -1
for i in range(1,n):
    if nodes[i] == k:
        find_node = i
    if nodes[i] > nodes[i-1] + 1:
        parent_node_idx += 1
    parent[i] = parent_node_idx

ans = 0
for i in range(n):
    if parent[parent[i]] == -1 or parent[parent[find_node]] == -1:
        continue

    if parent[i] != parent[find_node] and parent[parent[i]] == parent[parent[find_node]]:
        ans += 1
# print(parent)
print(ans)



    
