n = int(input())

alpha_to_index = {}
index_to_alpha = [""] * 27
indegree = [0] * 27
words = []
graph = [[] for _ in range(27)]

idx = 0
for _ in range(n):
    word = input()
    words.append(word)

for word in words:
    for char in word:
        if char not in alpha_to_index:
            idx += 1
            alpha_to_index[char] = idx
            index_to_alpha[idx] = char

for i in range(n-1):
    for j in range(min(len(words[i]), len(words[i+1]))):
        x, y = words[i][j], words[i+1][j]

        if x != y:
            graph[alpha_to_index[x]].append(alpha_to_index[y])
            indegree[alpha_to_index[y]] += 1
            break

from collections import deque
q = deque()

for i in range(1, idx+1):
    if indegree[i] == 0:
        q.append(i)

ans = []
is_inf = False
visited = [False] * (idx+1)
while q:
    if len(q) > 1:
        is_inf = True
    x = q.popleft()
    visited[x] = True
    ans.append(x)

    for y in graph[x]:
        indegree[y] -= 1
        if indegree[y] == 0:
            q.append(y)

is_cycle = False
for i in range(1,idx+1):
    if not visited[i]:
        is_cycle = True

if is_cycle:
    print(-1)
elif is_inf:
    print("inf")
else:
    for i in ans:
        print(index_to_alpha[i], end = "")

