n = int(input())
live = list(map(int, input().split()))
speed = list(map(int, input().split()))

left = 1
right = 10**9
ans = float('inf')

def check(p):
    max_time = 0
    for i in range(n):
        dist = abs(live[i] - p)
        go_time = dist / float(speed[i])
        max_time = max(max_time , go_time)

    return max_time < ans

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(f'{ans:.4f}')
