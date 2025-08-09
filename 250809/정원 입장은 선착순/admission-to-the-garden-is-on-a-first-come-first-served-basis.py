'''번호표 1~n n명의 사람
i번 사람은 a 시간에 입구 도착, t시간 머무르다 감
1명만 들어갈 수 있음
i번사람이 도착했을때 안에 사람있으면 나올떄까지 기다려야함 '''
import heapq
n = int(input())
people = []
for i in range(1,n+1):
    a,t = map(int, input().split())
    people.append((i,a,t))

people.sort(key = lambda x:x[1])
ans = 0
time = 0
waiting = []

i = 0
heapq.heappush(waiting, people[i])
i += 1
# print(people)

while waiting:
    id, a, t = heapq.heappop(waiting)
    
    wait_time = max(0, time-a)
    ans = max(ans, wait_time)
    time = a+t+wait_time
    # print(f'{id} 입장, 대기{wait_time}, 퇴장시간{time}')
    
    
    while i<n and people[i][1] <= time:
        heapq.heappush(waiting,  people[i])
        i += 1

    if i<n and not waiting and people[i][1] > time:
        heapq.heappush(waiting,  people[i])
        i += 1
    # print(waiting)

print(ans)