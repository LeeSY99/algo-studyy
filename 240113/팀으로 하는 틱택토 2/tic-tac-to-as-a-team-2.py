board=[list(int(x) for x in input()) for _ in range(3)]


team=[]
count=0
for b in board:
    if len(set(b))==2:
        if set(b) not in team:
            team.append(set(b))
            count+=1

for i in range(3):
    now=[]
    for j in range(3):
        now.append(board[j][i])
    if len(set(now))==2:
        if set(now) not in team:
            team.append(set(now))
            count+=1

now=[board[0][0],board[1][1],board[2][2]]
if len(set(now))==2:
    if set(now) not in team:
        team.append(set(now))
        count+=1

now=[board[0][2],board[1][1],board[2][0]]
if len(set(now))==2:
    if set(now) not in team:
        team.append(set(now))
        count+=1

print(count)