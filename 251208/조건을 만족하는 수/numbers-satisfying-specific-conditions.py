n = int(input())
word = list(input().split())
import heapq
indegree = [0] * (n+1)
graph = [[] for _ in range(n + 1)]

for i in range(n-1):
    char = word[i]
    num = i+1
    if char == '<':
        graph[num].append(num+1)
    else:
        graph[num+1].append(num)

def t_sort(r):
    ans = [0] * (n+1)
    q = []
    indegree = [0] * (n+1)
    for i in range(1, n+1):
        for x in graph[i]:
            indegree[x] += 1

    for i in range(1,n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i if not r else -i)
    cnt = 1
    while q:
        if not r:
            x = heapq.heappop(q)
        else:
            x = -heapq.heappop(q)
        
        ans[x] = cnt
        cnt+=1

        for y in graph[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                heapq.heappush(q, y if not r else -y)

    for i in range(1, n+1):
        print(f'{ans[i]:03d}', end = "")
    print()

t_sort(False)
t_sort(True)


        







