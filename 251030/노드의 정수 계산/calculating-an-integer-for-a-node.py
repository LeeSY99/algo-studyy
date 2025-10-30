n = int(input())
child = [[] for _ in range(n+1)]
res = [0] *(n+1)

for i in range(2,n+1):
    t,a,p = map(int, input().split())
    if t == 1:
        pass
    else:
        a = -a
    child[p].append((i,a))
    res[i] = a


def dfs(x):
    child_sum = res[x]
    for c, a in child[x]:
        dfs(c)
        child_sum += res[c]
    if child_sum < 0:
        res[x] = 0
    else:
        res[x] = child_sum
    

# print(res)  
dfs(1)
# print(child)
# print(res)
print(res[1])




    
