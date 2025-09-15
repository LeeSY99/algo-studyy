n, m = map(int, input().split())

points = [int(input()) for _ in range(n)]
points.sort()

left = 0
right = 10**9
#거리를 m으로 계산

def calc(dist):
    count = 1
    last_pos = 0
    for i in range(1,n):
        if points[i] - points[last_pos] >= dist:
            last_pos = i
            count += 1

    if count >= m:
        return True
    else:
        return False

    
ans = 0
while left <= right:
    mid = (left + right) // 2
    if calc(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1

print(ans)

