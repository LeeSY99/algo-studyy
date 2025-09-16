''' 1~N 번호표 든 n명의 사람
순서대로 무대에 올라 di시간 머무름
한번에 k명 올라감
먼저 무대 끝나면 내려가고 다음사람 올라옴

모든사람이 t_max시간을 넘지않을 때 가능한 k 최솟값''' 
import heapq

n, t_max = map(int, input().split())

time = []
for _ in range(n):
    d = int(input())
    time.append(d)

left = 1
right = 10000
ans = float('inf')

def check(k):
    stage = []
    count = 0
    last_time = 0
    for i in range(n):
        if count == k:
            count -= 1
            down_time = heapq.heappop(stage)
            last_time = max(last_time, down_time)
        
        heapq.heappush(stage, (time[i] + last_time))
        count += 1
    while stage:
        down_time = heapq.heappop(stage)
        last_time = max(last_time, down_time)
    return last_time <= t_max


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        right = mid - 1
        ans = min(ans, mid)
    else:
        left = mid + 1
print(ans)
