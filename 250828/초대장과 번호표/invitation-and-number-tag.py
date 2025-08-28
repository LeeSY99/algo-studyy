''' n명 / g개 그룹
같은 사람이 여러 그룹 가능
멤버가 일치하는 그룹은 없다
k명인 그룹에서 k-1명이 초대를 받음, 1명은 받아야함
1번사람은 무조건 초대장을 줌 
확실하게 초대장 받게 되는 인원 수 출력'''

n, g = map(int, input().split())
groups = [set() for _ in range(g)]  #그룹에 속한 사람 번호
people_groups = [[] for _ in range(n)]  #사람별로 어디 그룹에 속하는지

count = {}
for i in range(g):
    num, *people = map(int, input().split())
    for p in people:
        groups[i].add(p-1)
        people_groups[p-1].append(i)

from collections import deque
q = deque()
invited = [False] * n
invited[0] = True #첫번째사람은 항상 초다
q.append(0)
ans = 0
while q:
    x = q.popleft()
    ans +=1
    for g_num in people_groups[x]:
        groups[g_num].remove(x)
        if len(groups[g_num]) == 1:
            invite_p = list(groups[g_num])[0]
            if not invited[invite_p]:
                invited[invite_p] = True
                q.append(invite_p)

print(ans)



