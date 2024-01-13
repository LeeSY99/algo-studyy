n=int(input())

points=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1,n):
        x1,y1=points[i][0],points[i][1]
        x2,y2=points[j][0],points[j][1]

        dx=x2-x1
        dy=y2-y1
        ok=True
        if not(dx==0 or dy==0):
            ok= False


print(int(ok))