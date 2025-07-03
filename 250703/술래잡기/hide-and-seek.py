n, m, h, k = map(int, input().split())

grid = [[0]*n for _ in range(n)]

from collections import deque
thief = deque()
for _ in range(m):
    r, c, d = input().split()
    r = int(r)-1
    c = int(c)-1
    d = int(d)
    thief.append((r,c,d))

tree = [[0]*n for _ in range(n)]
for _ in range(h):
    r,c = map(int, input().split())
    tree[r-1][c-1] = 1

def in_range(r,c):
    return 0<=r<n and 0<=c<n

r1,c1 = n//2, n//2
grid[r1][c1] = 1
dr, dc = [-1,0,1,0],[0,1,0,-1]


# for r,c,d in thief:
#     grid[r][c] = 2

point = 0
d1 = 0
count = 0
max_count = 1
dir_count = 0
reverse = False
center = n//2
for turn in range(k):
    #도둑 이동
    for _ in range(len(thief)):
        r2,c2,d = thief.popleft()
        distance = abs(r1-r2) + abs(c1-c2)
        if distance <= 3:
            nr, nc = r2 +dr[d], c2+ dc[d]
            if in_range(nr,nc):
                if not (nr == r1 and nc == c1):
                    thief.append((nr,nc,d))
                else:
                    thief.append((r2,c2,d))
            else:
                d = (d+2)%4
                nr, nc = r2 +dr[d], c2+ dc[d]
                if in_range(nr, nc) and not (nr == r1 and nc == c1):
                    thief.append((nr,nc,d))
                else:
                    thief.append((r2,c2,d))
        else:
            thief.append((r2,c2,d))
    # 술래 이동   
    r1, c1 = r1+dr[d1] , c1+dc[d1]
    count+=1

    if not reverse:
        if count == max_count:
            dir_count +=1
            d1 = (d1+1)%4
            count = 0
            if dir_count == 2:
                max_count+=1
                dir_count = 0
    else:
        if count == max_count:
            dir_count +=1
            d1 = (d1-1)%4
            count = 0
            if dir_count == 2:
                max_count-=1
                dir_count = 0
    
    if r1 == 0 and c1 == 0:
        reverse = True
        d1=2
        count = 0
        dir_count = -1
        max_count = n-1
    elif r1 == center and c1 == center:
        reverse = False
        d1= 0
        count=0
        dir_count = 0
        max_count =1
    
    
    #체크
    for i in range(3):
        cr1, cc1 = r1+dr[d1]*i , c1+dc[d1]*i
        if not in_range(cr1,cc1):
            break
        for _ in range(len(thief)):
            r2,c2,d = thief.popleft()
            if cr1==r2 and cc1==c2 and not tree[cr1][cc1]:
                point += (turn+1)
            else:
                thief.append((r2,c2,d))
    

print(point)            




