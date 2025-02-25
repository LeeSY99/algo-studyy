n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

def in_range(i,j):
    return 0<=i<n and 0<=j<n

ans=0
for i in range(n):
    for j in range(n):
        for a in range(2,n): #세로길이
            for b in range(2,n): #가로길이
                num=0
                is_rec=True
                for h in range(a):
                    for l in range(b):
                        if (h==0) or (h==a-1) or (l==0) or (l==b-1):
                            if in_range(i+h-l,j+h+l):
                                num+=(grid[i+h-l][j+h+l])
                            else:
                                is_rec=False
                                break
                    if is_rec:
                        ans=max(ans,num)
                
        
            

print(ans)

