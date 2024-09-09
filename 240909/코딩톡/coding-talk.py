n,m,p=map(int,input().split())
info = [list(input().split()) for _  in range(m)]

people=[]
start='A'
for i in range(n):
    people.append(chr(ord(start)+i))

read=[]
not_read_msg=int(info[p-1][1])
for i in range(m):
    if i==p-1:
        if int(info[i][1])==0:  #안읽은 인원이 0이면 끝냄
            exit()
    if int(info[i][1])==not_read_msg or i>=p-1: 
# p번째 메시지의 안읽은 수가 이전 메시지에서와 같다면 이전 메시지를 보낸 사람도 p번째 메시지를 본 것. 역시 p번쨰 이후로 보낸 인원도 해당 메시지를 본 것
        read.append(info[i][0])

#안읽은 인원 필터링 및 정렬
ans=[]
for p in people:
    if p not in read:
        ans.append(p)
ans.sort()
for a in ans:
    print(a, end=' ')