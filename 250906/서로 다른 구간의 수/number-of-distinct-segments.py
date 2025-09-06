n = int(input())

segs = [tuple(map(int, input().split())) for _ in range(n)]

points = []
# for i, x1,x2 in enumerage(segs):
#     points.append((x1, 1, i))
#     points.append((x2, -1, i))

# points.sort()

# ans = 0
# seg = set()
# for x, v, idx in points:
#     if v == 1:
#         if not seg:
#             ans +=1
#         seg.add(index)
#     else:
#         seg.remove(index)

# print(ans)

for x1,x2 in segs:
    points.append((x1,1))
    points.append((x2,-1))

points.sort()
cnt = 0
ans = 0
for x, v in points:
    cnt += v
    if cnt == 0:
        ans += 1

print(ans)