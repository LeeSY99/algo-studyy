n,m=map(int,input().split())

arr=list(map(int,input().split()))

max_sum=0
for i in range(n):#시작위치
    now_sum=arr[i]
    next_index=arr[i]-1
    for _ in range(m-1):
        now_sum+=arr[next_index]
        next_index=arr[next_index]-1
    max_sum=max(max_sum,now_sum)

print(max_sum)