n,m,c = map(int, input().split())
time = list(map(int, input().split()))
time.sort()

left = 0
right = 10**9
ans = 10**9

def check(wait):
    start = float('-inf')
    bus_count = 0
    in_bus = 0
    for t in time:
        if t > start + wait or in_bus == c:
            start = t
            bus_count += 1
            in_bus = 1
        else:
            in_bus += 1
        
        
    return bus_count <= m
        
        



while left<= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)