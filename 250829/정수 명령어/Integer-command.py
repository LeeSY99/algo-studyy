t = int(input())

from sortedcontainers import SortedSet

for _ in range(t):
    ss = SortedSet()
    k = int(input())
    for i in range(k):
        cmd, n = input().split()
        n = int(n)
        if cmd == 'I':
            ss.add(n)
        elif cmd == 'D':
            if len(ss) == 0:
                continue
            if n == 1:
                ss.remove(ss[-1])
            elif n == -1:
                ss.remove(ss[0])
    if len(ss) == 0:
        print('EMPTY')
    else:
        print(ss[-1], ss[0])