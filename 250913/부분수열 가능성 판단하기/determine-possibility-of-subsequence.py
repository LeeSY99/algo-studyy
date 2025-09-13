n,m = map(int, input().split())

A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

L = [0] * (m+2)
R = [0] * (m+2)

i = 1
for j in range(1, m + 1):
    while i <= n and A[i] != B[j]: 
        i += 1
    L[j] = i
    if i <= n: 
        i += 1

i = n
for j in range(m, 0, -1):
    while i >= 1 and A[i] != B[j]:
        i -= 1
    R[j] = i
    if i >= 1: 
        i -= 1

R[m+1] = n+1

ans = 0
for j in range(1, m + 1):
    if L[j - 1] < R[j + 1]: 
        ans += 1

print(ans)

