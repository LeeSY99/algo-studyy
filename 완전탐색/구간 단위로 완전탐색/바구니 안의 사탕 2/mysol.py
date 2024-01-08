n,k=map(int,input().split())

candies=[0]*101

for _ in range(n):
    candy,i=map(int,input().split())
    candies[i]+=candy

max_count=0
if k<50:  #k가 50이 넘어가면 루프가 돌지 않는다.
    for c in range(k,101-k):
        candy_sum=0
        for i in range(c-k,c+k+1):
            candy_sum+=candies[i]
        max_count=max(max_count,candy_sum)
else:
    max_count=sum(candies)

print(max_count)