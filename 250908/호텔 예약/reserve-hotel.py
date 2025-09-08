n = int(input())
segs = [tuple(map(int, input().split())) for _ in range(n)]

points = []
for idx, (s, e )in enumerate(segs):
    points.append((s,1,idx))
    points.append((e,-1,idx))


points.sort(key = lambda x: (x[0], -x[1]))
ans = 0
room_count = 0



for x, v, idx in points:
    if v == 1:
        room_count += 1
    else:
        room_count -= 1

    ans = max(ans, room_count)

print(ans)