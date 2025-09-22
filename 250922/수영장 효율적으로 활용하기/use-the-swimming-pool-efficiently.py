n,m = map(int, input().split())
time = list(map(int, input().split()))

left = 0
right = 144000000
ans = float('inf')

def check(t):
    lane_count = 1
    lane_time = 0
    for i in range(n):
        if time[i] > t:
            return False
        if lane_time + time[i] > t:
            lane_count += 1
            lane_time = time[i]
        else:
            lane_time += time[i]

    return lane_count <= m


while left <= right:
    mid = (left + right) // 2
    
    if check(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)
    