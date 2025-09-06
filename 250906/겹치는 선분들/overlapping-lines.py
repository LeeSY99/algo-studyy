n, k = map(int, input().split())

now_x = 0
points = []

for i in range(1,n+1):
    x, dir = input().split()
    x = int(x)
    if dir == 'R':
        points.append((min(now_x, now_x + x), 1, i))
        points.append((max(now_x, now_x + x), -1, i))
        now_x += x
    else:
        points.append((min(now_x, now_x - x), 1, i))
        points.append((max(now_x, now_x - x), -1, i))
        now_x -= x

points.sort()

ans = 0
seg_cnt = 0
for x, v, num in points:
    seg_cnt += v
    if seg_cnt >= 2:
        ans += 1
            

print(ans)
    