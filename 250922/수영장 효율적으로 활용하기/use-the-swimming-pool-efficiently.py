n,m = map(int, input().split())
time = list(map(int, input().split()))

left = 0
right = 144000000
ans = float('inf')

def check(t):
    lane_count = 1
    j = 0
    max_time = 0
    lane_time = 0
    while j < n:
        if lane_time + time[j] <= t:
            lane_time += time[j]
        else:
            max_time = max(max_time, lane_time)
            lane_count += 1
            lane_time = time[j]
        j+=1
    max_time = max(max_time, lane_time)

    return lane_count <= m, max_time




while left <= right:
    mid = (left + right) // 2
    result, max_time = check(mid)
    if result:
        right = mid - 1
        ans = min(ans, max_time)
    else:
        left = mid + 1

print(ans)
    