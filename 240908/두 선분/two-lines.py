x1,x2,x3,x4 = map(int,input().split())

def check(x1,x2,x3,x4):
    intersect=1

    if x2<=x3:
        intersect=0
    elif x4<=x1:
        intersect=0
    
    if intersect:
        return 'intersecting'
    else:
        return 'nonintersecting'

print(check(x1,x2,x3,x4))