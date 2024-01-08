n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<m

def block1_1(nr,nc):#기본
    next1_x,next1_y=nr-1,nc
    next2_x,next2_y=nr,nc+1
    return next1_x,next1_y,next2_x,next2_y

def block1_2(nr,nc):#좌우로 뒤집음,90도3번
    next1_x,next1_y=nr-1,nc
    next2_x,next2_y=nr,nc-1
    return next1_x,next1_y,next2_x,next2_y

def block1_3(nr,nc):#상하로 뒤집음,90도1번
    next1_x,next1_y=nr,nc+1
    next2_x,next2_y=nr+1,nc
    return next1_x,next1_y,next2_x,next2_y

def block1_4(nr,nc):# 90도2번
    next1_x,next1_y=nr,nc-1
    next2_x,next2_y=nr+1,nc
    return next1_x,next1_y,next2_x,next2_y

    
def block2_1(nr,nc):#가로
    next1_x,next1_y,next2_x,next2_y=nr,nc+1,nr,nc+2
    return next1_x,next1_y,next2_x,next2_y    
def block2_2(nr,nc):#세로
    next1_x,next1_y,next2_x,next2_y=nr+1,nc,nr+2,nc
    return next1_x,next1_y,next2_x,next2_y   

max_val=0
for nr in range(n):
    for nc in range(m):
        next1_x,next1_y,next2_x,next2_y = block1_1(nr,nc)
        if in_range(next1_x,next1_y) and in_range(next2_x,next2_y):
            now_val=arr[nr][nc]+arr[next1_x][next1_y]+arr[next2_x][next2_y]
            if now_val>max_val:
                max_val=now_val
       
        next1_x,next1_y,next2_x,next2_y = block1_2(nr,nc)
        if in_range(next1_x,next1_y) and in_range(next2_x,next2_y):
            now_val=arr[nr][nc]+arr[next1_x][next1_y]+arr[next2_x][next2_y]
            if now_val>max_val:
                max_val=now_val
        
        next1_x,next1_y,next2_x,next2_y = block1_3(nr,nc)
        if in_range(next1_x,next1_y) and in_range(next2_x,next2_y):
            now_val=arr[nr][nc]+arr[next1_x][next1_y]+arr[next2_x][next2_y]
            if now_val>max_val:
                max_val=now_val
        
        next1_x,next1_y,next2_x,next2_y = block1_4(nr,nc)
        if in_range(next1_x,next1_y) and in_range(next2_x,next2_y):
            now_val=arr[nr][nc]+arr[next1_x][next1_y]+arr[next2_x][next2_y]
            if now_val>max_val:
                max_val=now_val
        
        next1_x,next1_y,next2_x,next2_y = block2_1(nr,nc)
        if in_range(next1_x,next1_y) and in_range(next2_x,next2_y):
            now_val=arr[nr][nc]+arr[next1_x][next1_y]+arr[next2_x][next2_y]
            if now_val>max_val:
                max_val=now_val
        
        next1_x,next1_y,next2_x,next2_y = block2_2(nr,nc)
        if in_range(next1_x,next1_y) and in_range(next2_x,next2_y):
            now_val=arr[nr][nc]+arr[next1_x][next1_y]+arr[next2_x][next2_y]
            if now_val>max_val:
                max_val=now_val
print(max_val)


