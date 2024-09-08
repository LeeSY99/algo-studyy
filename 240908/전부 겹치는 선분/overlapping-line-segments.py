n=int(input())

points=[list(map(int, input().split())) for _ in range(n)]

for i in range(1,101):
    can=1
    for j in range(n):
        if i<points[j][0]:
            can=0
            break
        if i>points[j][1]:
            can=0
            break
    if can:
        print('Yes')
        exit()

print('No')