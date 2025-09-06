n, k = map(int, input().split())

now_x = 0
points = []

for i in range(1,n+1):
    x, dir = input().split()
    x = int(x)
    if dir == 'R':
        points.append((min(now_x, now_x + x), 1))
        points.append((max(now_x, now_x + x), -1))
        now_x += x
    else:
        points.append((min(now_x, now_x - x), 1))
        points.append((max(now_x, now_x - x), -1))
        now_x -= x

points.sort()
# print(points)
ans = 0
seg_cnt = 0
start = float('-inf')
for x, v in points:
    seg_cnt += v
    if seg_cnt >= 2:
        if start == float('-inf'):
            start = x
    else:
        if start != float('-inf'):
            ans += x - start
            start = float('-inf')
            

print(ans)
    