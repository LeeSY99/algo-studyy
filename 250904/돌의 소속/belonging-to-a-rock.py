n,q = map(int, input().split())

group = [0] * (n+1)

for i in range(1,n+1):
    g = int(input())
    group[i] = g

group_sum = [[0] * (n+1) for _ in range(4)]


for g in range(1,4):
    for i in range(1,n+1):
        val = 0
        if g == group[i]:
            val = 1

        group_sum[g][i] = group_sum[g][i-1] + val

def get_value(g, a,b ):
    return group_sum[g][b] - group_sum[g][a-1]

for _ in range(q):
    a,b = map(int, input().split())
    print(get_value(1,a,b),get_value(2,a,b),get_value(3,a,b))