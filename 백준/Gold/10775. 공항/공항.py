g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    A = find(a)
    B = find(b)
    parent[A] = B

ans = 0
for i in range(1, p+1):
    g_i = int(input())
    j = find(g_i)
    if j == 0:
        break
    ans += 1
    union(j, j-1)

print(ans)
