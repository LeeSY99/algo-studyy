''' n명 / g개 그룹
같은 사람이 여러 그룹 가능
멤버가 일치하는 그룹은 없다
k명인 그룹에서 k-1명이 초대를 받음, 1명은 받아야함
1번사람은 무조건 초대장을 줌 
확실하게 초대장 받게 되는 인원 수 출력'''

n, g = map(int, input().split())
groups = []
invited = set([1])
for _ in range(g):
    num, *people = map(int, input().split())
    for p in people:
        if p not in invited:
            invited.add(p)
            break

print(len(invited))

