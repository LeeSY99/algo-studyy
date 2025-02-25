n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

def in_range(i,j):
    return 0<=i<n and 0<=j<n

ans=0
for i in range(n):
    for j in range(n):
        if in_range(i,j) and in_range(i-1,j-1):
            rec=grid[i][j] + grid[i-1][j-1]
            # is_rec=False
            for k in range(1,n):
                if in_range(i-k,j+k) and in_range(i-1-k,j-1+k):
                    is_rec=True
                    rec +=(grid[i-k][j+k] + grid[i-1-k][j-1+k])
                    ans = max(ans, rec)

print(ans)

