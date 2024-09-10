a,b,x,y = map(int,input().split())

import sys
min_dist=sys.maxsize

#1) a->b
min_dist=min(min_dist, abs(b-a))
#2) a->x->y->b
min_dist=min(min_dist, abs(x-a) + abs(b-y))
#3) a->y->x->b
min_dist=min(min_dist, abs(y-a) + abs(b-x))

print(min_dist)