n, k = map(int,input().split())

from collections import deque

myqueue = deque()
for i in range(1,n+1):
    myqueue.append(i)

while (len(myqueue) != 0):
    for i in range(k-1):
        myqueue.append(myqueue.popleft())
    print(myqueue.popleft(), end=' ')
