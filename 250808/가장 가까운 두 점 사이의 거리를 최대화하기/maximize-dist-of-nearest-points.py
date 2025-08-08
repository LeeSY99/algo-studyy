'''  선분 위 하나 점을 잡아 x축 기준으로
가장 가까운 두 점 사이의 거리 최대화
'''

n = int(input())

lines = []
for _ in range(n):
    x1,x2 = map(int, input().split())
    lines.append((x1,x2))

lines.sort()

def check(dist):
    count = 0
    cur = 0

    for x1, x2 in lines:
        if cur < x1:
            cur = x1
        if cur > x2:
            return False

        cur = cur + dist

    return True

left = 1
right = 10**9
ans = 0

while left<=right:
    mid = (left+right)//2

    if check(mid):
        left = mid+1
        ans = max(ans, mid)

    else:
        right = mid-1

print(ans)
