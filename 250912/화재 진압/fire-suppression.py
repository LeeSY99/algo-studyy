n,m = map(int, input().split())

fire = list(map(int, input().split()))
station = list(map(int, input().split()))
fire.sort()
station.sort()


i = 0
j = 0
ans = 0
def dist(i, j):
    return abs(fire[i] - station[j])
    
for i in range(n):
    while j<m-1 and dist(i,j) > dist(i,j+1):
        j+=1
    ans = max(ans, dist(i,j))

print(ans)
    


