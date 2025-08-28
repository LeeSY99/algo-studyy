n = int(input())

from sortedcontainers import SortedSet
ss = SortedSet()

for _ in range(n):
    cmd, *r = input().split()

    if cmd == 'add':
        x = int(r[0])
        ss.add(x)
    elif cmd == 'remove':
        x = int(r[0])
        ss.remove(x)
    elif cmd == 'find':
        x = int(r[0])
        if x in ss:
            print('true')
        else:
            print('false')
    elif cmd == 'lower_bound':
        x = int(r[0])
        idx = ss.bisect_left(x)
        
        print(ss[idx] if idx < len(ss) else None)
    elif cmd == 'upper_bound':
        x = int(r[0])
        idx = ss.bisect_right(x)
        # print('upperbound', idx)
        print(ss[idx] if idx < len(ss) else None)

    elif cmd == 'largest':
        if len(ss) == 0:
            print(None)
        else:
            print(ss[-1])

    elif cmd == 'smallest':
        if len(ss) == 0:
            print(None)
        else:
            print(ss[0])
