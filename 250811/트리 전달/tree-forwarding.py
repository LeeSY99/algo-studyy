'''
i w -> i번 노드에서 점수 w획득, 
        자식노드들을 c라하면 c w연산 수행 '''


n, m = map(int, input().split())

parent = list(map(int, input().split()))

score = [0] * (n+1)
def calc(x, w):
    score[x] += w
    for idx, p in enumerate(parent,1):
        if p == x:
            calc(idx,w)


for _ in range(m):
    i, w = map(int, input().split())
    calc(i,w)
    
print(*score[1:])