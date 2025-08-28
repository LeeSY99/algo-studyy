n = int(input())

s = set()

for _ in range(n):
    cmd, x = input().split()
    x = int(x)

    if cmd == 'add':
        s.add(x)
    elif cmd == 'remove':
        s.remove(x)
    else:
        if x in s:
            print('true')
        else:
            print('false')