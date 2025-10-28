n,q = map(int, input().split())
visited = {}

def search(x):
    start = x
    v = []
    while x != 1:
        x = x//2
        if x in visited:
            v.append(x)
    if not v:
        visited[start] = True
        return 0
    else:
        v.sort()
        return v[0]


for _ in range(q):
    goal = int(input())
    print(search(goal))