n=int(input())

games=[list(map(int,input().split())) for _ in range(n)]



#가위 바위 보
max_win=0
g1=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==3:
        g1+=1
    if games[i][0]==2 and games[i][1]==1:
        g1+=1
    if games[i][0]==3 and games[i][1]==2:
        g1+=1
max_win=max(max_win,g1)

#가위 보 바위
g1=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==2:
        g1+=1
    if games[i][0]==2 and games[i][1]==3:
        g1+=1
    if games[i][0]==3 and games[i][1]==1:
        g1+=1
max_win=max(max_win,g1)

#바위 가위 보
g1=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==2:
        g1+=1
    if games[i][0]==2 and games[i][1]==3:
        g1+=1
    if games[i][0]==3 and games[i][1]==1:
        g1+=1
max_win=max(max_win,g1)

#바위 보 가위
g1=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==3:
        g1+=1
    if games[i][0]==2 and games[i][1]==1:
        g1+=1
    if games[i][0]==3 and games[i][1]==2:
        g1+=1
max_win=max(max_win,g1)

#보 가위 바위
g1=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==3:
        g1+=1
    if games[i][0]==2 and games[i][1]==1:
        g1+=1
    if games[i][0]==3 and games[i][1]==2:
        g1+=1
max_win=max(max_win,g1)

#보 바위 가위
g1=0
for i in range(n):
    if games[i][0]==1 and games[i][1]==2:
        g1+=1
    if games[i][0]==2 and games[i][1]==3:
        g1+=1
    if games[i][0]==3 and games[i][1]==1:
        g1+=1
max_win=max(max_win,g1)

print(max_win)