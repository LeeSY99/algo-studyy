n=int(input())

nums=[[0]*n for _ in range(n)]

r,c=n//2,n//2
num=1
nums[r][c]=num
index=0

move_count=1

def in_range(r,c):
    return 0<= r and r<n and 0<=c and c<n

def move():
    global r,c
    dr,dc=[0,-1,0,1],[1,0,-1,0]
    r,c=r+dr[index],c+dc[index]

def end():
    return not in_range(r,c)
count=1

while not end():
    for _ in range(move_count):
        nums[r][c]=count
        count+=1
        move()
        if end():
            break
    index=(index+1)%4
    if index ==0 or index==2:
        move_count+=1

for n in nums:
    print(*n)
