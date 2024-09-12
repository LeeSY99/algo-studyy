n=int(input())

in_data=list(input())
import sys
#나의 풀이 O(n^3) 
# max_interval=0

# for i in range(n):
#     desk=in_data[:]
#     if desk[i]=='1':
#         continue
#     desk[i]='1'

#     min_interval=sys.maxsize
#     for j in range(n):
#         for k in range(j+1,n):
#             if desk[j]=='1' and desk[k]=='1':
#                 min_interval=min(min_interval,k-j)
#                 break
#     max_interval=max(max_interval,min_interval)

# print(max_interval)

#O(n^2)인 풀이

max_dist=0
max_i, max_j = -1,-1
for i in range(n):
    for j in range(i+1,n):
        if in_data[i]=='1' and in_data[j]=='1': #차 있는 좌석 사이 거리 구하고 i,j위치 기억
            max_dist=max(max_dist,j-i)
            max_i,max_j = i,j
            break

#맨 앞 자리 비어있는 경우 새 인원을 맨 앞자리에 배치하는 경우
max_dist2=-1
max_idx = -1
if in_data[0]=='0':
    dist=0
    for i in range(n):
        if in_data[i]=='1':
            break
        dist+=1
    if dist>max_dist2:
        max_dist2=dist
        max_idx=0

#맨 뒷자리 비어있는 경우, 맨 뒷자리에 배치
if in_data[n-1]=='0':
    dist=0
    for i in range(n-1,-1,-1):
        if in_data[i]=='1':
            break
        dist+=1
    if dist> max_dist2:
        max_dist2=dist
        max_idx=n-1

#최적의 자리에 1로 변환
if max_dist2 >= max_dist//2:
    in_data[max_idx]='1'
else:
    in_data[(max_i + max_j)//2] = '1'

ans=sys.maxsize
for i in range(n):
    for j in range(i+1,n):
        if in_data[i]=='1' and in_data[j]=='1':
            ans=min(ans, j-i)
            break
print(ans)