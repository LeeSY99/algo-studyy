n,m = map(int, input().split())

time = []
for _ in range(m):
    a = int(input())
    time.append(a)

left = 1
right = 10**14
ans = 10**14

def check(mid):
    ps = 0
    for t in time:
        ps += mid//t

    return ps

while left <= right:
    mid = (left + right) //2


    if check(mid) >= n:
        ans = min(ans, mid)
        right = mid -1
    else:
        left = mid + 1

print(ans)