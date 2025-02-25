n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!

def search(i,j,k,l):
    for r in range(i,k+1):
        for c in range(j,l+1):
            if grid[r][c]<0:
                return False
    return True


ans=0
for i in range(n): #(i,j), (k,l)
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                if search(i,j,k,l):
                    ans=max(ans, (k-i+1)*(l-j+1))

print(ans)


