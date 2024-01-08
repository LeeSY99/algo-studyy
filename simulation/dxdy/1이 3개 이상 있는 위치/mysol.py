n=int(input())

nums=[]
for _ in range(n):
    nums.append(list(map(int,input().split())))

dr=[0,1,0,-1]
dc=[1,0,-1,0]
answer=0
def in_range(nr,nc):
    return 0<=nr<n and 0<=nc<n

for i in range(n):
    for j in range(n):
        count=0
        for a,b in zip(dr,dc):
            nr,nc = i+a, j+b
            if in_range(nr,nc):
                if nums[nr][nc]==1:
                    count+=1
        if count>=3:
            answer+=1

print(answer)
#O(n^2)