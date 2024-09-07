n,l = map(int,input().split())
nums = list(map(int,input().split()))
#나의 코드

# for max_num in range(100,-1,-1): #예상 H값 완전 탐색
#     plus_count= #1을 더한 횟수
#     for i in range(n):    #nums배열을 순회하면서 예상H값보다 1작으면 1을 더함
#         if nums[i]==max_num-1:
#             nums[i]+=1
#             plus_count+=1
#         if plus_count==l: #l횟수 다쓰면 nums배열 순회 종료하고 조건에 만족하는지 확인
            # break
#     count=0
#     for j in range(n):
#         if nums[j]>=max_num:
#             count+=1
#     if count>=max_num:
#         print(max_num)
#         break

##정답코드
ans=0
for i in range(1,n+1):
    count=0
    plus_count=0

    for j in range(n):
        if nums[j]>=i:
            count+=1
        elif nums[j]==i-1:
            if plus_count<l:
                plus_count+=1
                count+=1
    if count>=i:
        ans=i
print(ans)
