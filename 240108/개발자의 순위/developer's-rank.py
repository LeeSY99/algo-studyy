k,n=map(int,input().split())
board=[]

for _ in range(k):
    a,b,c,d=map(int,input().split())
    board.append((a,b,c,d))

count=0
for i in range(n):
    for j in range(i+1,n):
        before=board[0][i]
        after=board[0][j]
    
        ok=True    
        for k in range(1,len(board)):
            for l in range(n):
                if board[k][l]==before:
                    first=l
                elif board[k][l]==after:
                    second=l
            if first>second:
                ok=False
        if ok:
            count+=1
print(count)