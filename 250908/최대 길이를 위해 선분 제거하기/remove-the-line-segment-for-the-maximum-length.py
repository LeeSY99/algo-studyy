n = int(input())

segs = [tuple(map(int, input().split())) for _ in range(n)]

points = []

for idx, (a, b) in enumerate(segs):
    points.append((a, 1, idx))
    points.append((b, -1, idx))

points.sort()

weights = [0] * n #해당 선분 제외시 영향을 주는 정도 -> 걸친 선분이 1개일 때 x-직전x값 
segs = set()
total_len = 0
ans = 0
prev_x = -1

for x, v, idx in points:
    seg_count = len(segs)
    if seg_count > 0: #총 길이 더함, 구간이 1개 이상일때
        total_len += x-prev_x

    if seg_count == 1:  # 해당 선분이 빠졌을 떄 전체 길이에서 얼마큼 빠지는지 -> 구간이 딱 1개일떄
        target_index = list(segs)[0]
        weights[target_index] += x - prev_x

    if v == 1:
        segs.add(idx)
    else:
        segs.remove(idx)
    prev_x = x

for weight in weights:
    ans = max(ans, total_len-weight)
print(ans)