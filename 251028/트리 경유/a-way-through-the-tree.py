n,q = map(int, input().split())
visited = [False] * (2**20+1)
# print(2**20)

def search(x):
    start = x
    v = []
    while start != 1:
        if visited[start]:
            v.append(start)
        start = start//2
    
    if not v:
        visited[x] = True
        return 0
    else:
        v.sort()
        return v[0]


for _ in range(q):
    goal = int(input())
    print(search(goal))