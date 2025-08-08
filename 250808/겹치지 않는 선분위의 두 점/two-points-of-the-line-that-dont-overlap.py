n,m = map(int, input().split())

points = []

for _ in range(m):
    a, b = map(int, input().split())
    points.append((a,b))

left = 0
right = 10**18
ans = 0

points.sort()

def check(dist):
    placed = 0
    cur = -1

    for a,b in points:
        if cur < a:
            cur = a
        if cur > b:
            continue

        while cur <=b:
            placed += 1
            if placed >= n:
                return True   
            cur = cur + dist
         
    return False



while left <= right:
    mid = (left+right) // 2
    if check(mid):
        left = mid+1
        ans = max(ans,mid)
    else:
        right = mid-1

print(ans)
