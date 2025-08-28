''' n명 / g개 그룹
같은 사람이 여러 그룹 가능
멤버가 일치하는 그룹은 없다
k명인 그룹에서 k-1명이 초대를 받음, 1명은 받아야함
1번사람은 무조건 초대장을 줌 
확실하게 초대장 받게 되는 인원 수 출력'''

n, g = map(int, input().split())

groups = [set() for _ in range(g)]  # 그룹에 누가 있는지
people_group = [[] for _ in range(n)] #사람이 어디 그룹에 있는지

for i in range(g):
    num, *people = map(int, input().split())

    for p in people:
        p -= 1
        groups[i].add(p)
        people_group[p].append(i)

from collections import deque
q = deque()
q.append(0)
invited = set([0]) # 초대받은 사람
ans = 0
while q:
    x = q.popleft()
    ans += 1
    for group_num in people_group[x]:
        groups[group_num].remove(x)

        if len(groups[group_num]) == 1:
            last = list(groups[group_num])[0]
            if last not in invited:
                invited.add(last)
                q.append(last)

print(ans)