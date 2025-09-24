from sortedcontainers import SortedSet
c,n = map(int, input().split())
red = [int(input()) for _ in range(c)]
black = []
for _ in range(n):
    a,b = map(int, input().split())
    black.append((b,a))

red_set = SortedSet(red)
black.sort()

ans = 0

for b, a in black:
    idx = red_set.bisect_left(a)
    if idx != len(red_set):
        r = red_set[idx]
        if r <= b:
            red_set.remove(r)
            ans += 1

    
print(ans)

