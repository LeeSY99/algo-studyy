a,b =map(int,input().split())
c,d=map(int,input().split())

intersect=1
if b < c or d < a:
    intersect=0

if intersect:
    if a>c:
        ans=(d-c)+(b-a)-(d-a)
    if a<c:
        ans=(d-c)+(b-a)-(b-c)
else:
    ans=(d-c)+(b-a)
    

print(ans)