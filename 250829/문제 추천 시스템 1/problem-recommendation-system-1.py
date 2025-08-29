n= int(input())

from sortedcontainers import SortedSet
ss = SortedSet()

for _ in range(n):
    p, l = map(int, input().split())
    ss.add((l,p))

m = int(input())
for _ in range(m):
    cmd, *remain = input().split()
    if cmd == 'rc':
        x = int(remain[0])
        if x == 1:
            print(ss[-1][1])
        if x == -1:
            print(ss[0][1])

    if cmd == 'ad':
        p, l = int(remain[0]), int(remain[1])
        idx = ss.bisect_left((l,p))
        if idx != len(ss):
            if ss[idx] == (l,p):
                ss.remove((l,p))
        ss.add((l,p))
    
    if cmd == 'sv':
        p, l = int(remain[0]), int(remain[1])
        ss.remove((l,p))
