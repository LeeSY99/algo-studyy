n,m = map(int, input().split())

fire = list(map(int, input().split()))
station = list(map(int, input().split()))

def can_go(i,j):
    if i == 0:
        return True
    if abs(fire[i] - station[j]) < abs(fire[i-1]-station[j]):
        return True
    if j == m-1:
        return True
    return False

i = 0
ans = 0
for j in range(m):
    while i<n and can_go(i,j):
        ans = max(ans, abs(fire[i] - station[j]))
        i+=1
    if i == n:
        break
print(ans)
