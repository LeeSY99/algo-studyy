from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

for _ in range(n):
    cmd, *remain = input().split()
    if cmd == 'add':
        k = int(remain[0])
        v = int(remain[1])

        sd[k] = v
    
    elif cmd == 'remove':
        k = int(remain[0])
        sd.pop(k)

    elif cmd == 'find':
        k = int(remain[0])
        if k in sd:
            print(sd[k])
        else:
            print(None)
        
    elif cmd == 'print_list':
        if len(sd) == 0:
            print(None)
        else:
            for key, value in sd.items():
                print(value, end = ' ')
        print()

