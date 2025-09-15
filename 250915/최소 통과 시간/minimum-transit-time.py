n,m = map(int, input().split())

time = []
for _ in range(m):
    a = int(input())
    time.append(a)

left = 1
right = 10**14
ans = 10**14

time.sort()

def check(mid):
    cnt = 0
    for t in time:
        cnt += mid // t

    if cnt >= n:
        return True
    else:
        return False


while left<=right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1

print(ans)
