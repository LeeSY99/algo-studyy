from collections import deque

mydeque=deque()

n=int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        mydeque.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        mydeque.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(mydeque.popleft())
    elif cmd[0] == 'pop_back':
        print( mydeque.pop())
    elif cmd[0] == 'size':
        print( len(mydeque))
    elif cmd[0] == 'empty':
        print( int(not mydeque))
    elif cmd[0] == 'front':
        print( mydeque[0])
    elif cmd[0] == 'back':
        print( mydeque[-1])

    
