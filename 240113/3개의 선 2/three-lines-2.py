n=int(input())

points=[list(map(int,input().split())) for _ in range(n)]

can=0
for i in range(11):
    for j in range(11):
        for k in range(11):
            ok=True
            for x,y in points:
                if x==i or x==j or x==k:
                    continue
                ok=False
            if ok:
                can=1
            
            ok=True
            for x,y in points:
                if x==i or x==j or y==k:
                    continue
                ok=False
            if ok:
                can =1

            ok=True
            for x,y in points:
                if x==i or y==j or y==k:
                    continue
                ok=False
            if ok:
                can =1

            ok=True
            for x,y in points:
                if y==i or y==j or y==k:
                    continue
                ok=False
            if ok:
                can =1

print(can)