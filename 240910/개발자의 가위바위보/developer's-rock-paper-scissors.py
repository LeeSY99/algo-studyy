n=int(input())

games=[list(map(int,input().split())) for _ in range(n)]


#내가 푼 일일이 비교하는 방식보다는
#1) 1>2 2>3 3>1
#2> 1>3 3>2 2>1
#2가지 경우로 (1,2), (2,3), (3,1)인 것을 찾으면 됨 아래도 마찬가지

#1)
max_win=0
win=0
for a,b in games:
    if a==1 and b==2:
        win+=1
    elif a==2 and b==3:
        win+=1
    elif a==3 and b==1:
        win+=1
max_win=max(max_win,win)

#2)
win = 0
for a, b in games:
    if a == 1 and b == 3:
        win += 1
    elif a == 3 and b == 2:
        win += 1
    elif a == 2 and b == 1:
        win += 1

max_win = max(max_win, win)

print(max_win)

# #가위 바위 보
# max_win=0
# g1=0
# for i in range(n):
#     if games[i][0]==1 and games[i][1]==3:
#         g1+=1
#     if games[i][0]==2 and games[i][1]==1:
#         g1+=1
#     if games[i][0]==3 and games[i][1]==2:
#         g1+=1
# max_win=max(max_win,g1)

# #가위 보 바위
# g1=0
# for i in range(n):
#     if games[i][0]==1 and games[i][1]==2:
#         g1+=1
#     if games[i][0]==2 and games[i][1]==3:
#         g1+=1
#     if games[i][0]==3 and games[i][1]==1:
#         g1+=1
# max_win=max(max_win,g1)

# #바위 가위 보
# g1=0
# for i in range(n):
#     if games[i][0]==1 and games[i][1]==2:
#         g1+=1
#     if games[i][0]==2 and games[i][1]==3:
#         g1+=1
#     if games[i][0]==3 and games[i][1]==1:
#         g1+=1
# max_win=max(max_win,g1)

# #바위 보 가위
# g1=0
# for i in range(n):
#     if games[i][0]==1 and games[i][1]==3:
#         g1+=1
#     if games[i][0]==2 and games[i][1]==1:
#         g1+=1
#     if games[i][0]==3 and games[i][1]==2:
#         g1+=1
# max_win=max(max_win,g1)

# #보 가위 바위
# g1=0
# for i in range(n):
#     if games[i][0]==1 and games[i][1]==3:
#         g1+=1
#     if games[i][0]==2 and games[i][1]==1:
#         g1+=1
#     if games[i][0]==3 and games[i][1]==2:
#         g1+=1
# max_win=max(max_win,g1)

# #보 바위 가위
# g1=0
# for i in range(n):
#     if games[i][0]==1 and games[i][1]==2:
#         g1+=1
#     if games[i][0]==2 and games[i][1]==3:
#         g1+=1
#     if games[i][0]==3 and games[i][1]==1:
#         g1+=1
# max_win=max(max_win,g1)

# print(max_win)