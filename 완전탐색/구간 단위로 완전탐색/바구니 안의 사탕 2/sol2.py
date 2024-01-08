n,k=map(int,input().split())

candies=[0]*101

for _ in range(n):
    candy,i=map(int,input().split())
    candies[i]+=candy

max_count=0
for i in range(100):
    candy_sum=0
    for j in range(i-k, i+k+1):
        if j>=0 and j<=100:
            candy_sum+=candies[j]
    max_count=max(max_count,candy_sum)

print(max_count)
#