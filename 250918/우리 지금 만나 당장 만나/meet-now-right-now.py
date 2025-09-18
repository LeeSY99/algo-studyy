n = int(input())
live = list(map(int, input().split()))
speed = list(map(int, input().split()))

left = 0
right = 10**9
ans = float('inf')

def check(time):
    max_time = 0
    min_x = live[0] - speed[0] * time
    max_x = live[0] + speed[0] * time
    for i in range(1, n):
        if live[i] - speed[i] * time > max_x or live[i] + speed[i] * time < min_x:
            return False
    return True


for i in range(100):
    mid = (left + right) / 2
    if check(mid):
        right = mid
        ans = min(ans, mid)
    else:
        left = mid

print(f'{ans:.4f}')
