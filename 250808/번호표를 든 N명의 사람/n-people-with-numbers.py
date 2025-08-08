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


def check(people):
    q = []
    for t in time:
        heapq.heappush(q,t)

    for i in range(people, n):
        cur_time = heapq.heappop(q)
        heapq.heappush(q, cur_time + time[i])

    
    end_time = 0
    while q:
        end_time = max(end_time, heapq.heappop(q))

    return end_time <= t_max

left = 1
right = n
ans = n

while left<=right:
    mid = (left+right)//2
    if check(mid):
        right = mid-1
        ans = min(ans, mid)
    else:
        left = mid+1
    
print(ans)



