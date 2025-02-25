n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Write your code here!
def in_range(i,j):
    return 0 <= i <n and 0 <= j <n

def diamond(i,j,k): #마름모 탐색
    gold=0
    for a in range(n):
        for b in range(n):
            if abs(a-i) + abs(b-j) <= k:
                if grid[a][b]:
                    gold+=1
    return gold


ans=0
for k in range(n):
    for i in range(n):
        for j in range(n): ##중심점 
            gold=diamond(i,j,k)
            if gold * m >= k**2 + (k+1)**2:
                ans = max(ans,gold)

print(ans)
        
