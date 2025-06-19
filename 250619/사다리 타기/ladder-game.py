n, m = map(int, input().split())

line=[]
for _ in range(m):
    ai, bi = map(int, input().split())
    line.append((ai,bi))

normal = [a for a in range(1,n+1)]
line.sort(key = lambda x:x[1])
for ai,bi in line:
    normal[ai-1], normal[ai] = normal[ai], normal[ai-1]

choose = []
ans = m
def backtrack(count):
    global choose
    global ans
    if count == m:
        after = move(choose)
        if after == normal:
            ans = min(ans, sum(choose))
        return

    for i in range(2):
        choose.append(i)
        backtrack(count+1)
        choose.pop()


def move(choose):
    selected = []
    after = [a for a in range(1,n+1)]
    for i in range(m):
        if choose[i] ==1:
            selected.append(line[i])
    for ai,bi in selected:
        after[ai-1], after[ai] = after[ai], after[ai-1]
    return after


backtrack(0)
print(ans)