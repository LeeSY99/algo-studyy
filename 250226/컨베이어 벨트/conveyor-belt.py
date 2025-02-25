n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Write your code here!


for _ in range(t):
    e1=u[-1]
    for i in range(n-1,0,-1):
        u[i]=u[i-1]

    e2=d[-1]
    for i in range(n-1,0,-1):
        d[i]=d[i-1]
    u[0]=e2
    d[0]=e1

print(*u)
print(*d)