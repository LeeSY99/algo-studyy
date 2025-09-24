n = int(input())
arr= [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: x[1])

this_end = 0
ans = 0
for s, e in arr:
    if s >=this_end:
        this_end = e
    else:
        ans += 1

print(ans)