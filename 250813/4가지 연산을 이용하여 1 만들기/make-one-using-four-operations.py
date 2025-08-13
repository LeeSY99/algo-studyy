import sys
from collections import deque

n = int(input())
arr = [sys.maxsize]*(2*n)
arr[n] = 0
visited = [False]*(2*n)

q = deque()
q.append(n)
visited[n] = True

def in_range(num):
    return 0<num<2*n
    
while q:
    now = q.popleft()
    if in_range(now-1) and not visited[now-1]:
        visited[now-1] = True
        q.append(now-1)
        arr[now-1] = arr[now] + 1
    
    if in_range(now+1) and not visited[now+1]:
        visited[now+1] = True
        q.append(now+1)
        arr[now+1] = arr[now] + 1

    if now%2 == 0 and in_range(now//2) and not visited[now//2]:
        visited[now//2] = True
        q.append(now//2)
        arr[now//2] = arr[now] + 1

    if now%3 == 0 and in_range(now//3) and not visited[now//3]:
        visited[now//3] = True
        q.append(now//3)
        arr[now//3] = arr[now] + 1

print(arr[1])