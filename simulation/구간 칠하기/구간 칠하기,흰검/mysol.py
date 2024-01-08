n=int(input())

white_count=[0]*200001
black_count=[0]*200001
offset=100000

block=[-1]*200001
WHITE=0
BLACK=1
GRAY=2

segment=[]
now=0
for _ in range(n):
    x,direction=input().split()
    x=int(x)

    if direction=='L':
            left=now-x+1
            right=now
            now=now-x+1
    elif direction=='R':
            left=now
            right=now+x-1
            now=now+x-1
    segment.append([left,right,direction])

for x1,x2,d in segment:
    x1,x2=x1+offset, x2+offset
    if d=='R':
        for i in range(x1,x2+1):
            black_count[i]+=1
            block[i]=BLACK
            if white_count[i]>=2 and black_count[i]>=2:
                block[i]=GRAY
    elif d=='L':
        for i in range(x1,x2+1):
            white_count[i]+=1
            block[i]=WHITE
            if white_count[i]>=2 and black_count[i]>=2:
                block[i]=GRAY

white_block=0
black_block=0
gray_block=0

for a in block:
    if a==WHITE:
        white_block+=1
    elif a==BLACK:
        black_block+=1
    elif a==GRAY:
        gray_block+=1
print(white_block,black_block,gray_block)

