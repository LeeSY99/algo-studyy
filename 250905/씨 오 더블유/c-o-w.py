n = int(input())

arr = list(input())

L = [0] * n
R = [0] * n

for i in range(n):
    if arr[i] == 'C':
        L[i] = 1
    if i > 0:
        L[i] += L[i-1]

for i in range(n-1,-1,-1):
    if arr[i] == 'W':
        R[i] = 1
    if i<n-1:
        R[i] += R[i+1]

count = 0
for i in range(n):
    if arr[i] == 'O':
        count += L[i-1] * R[i+1]

print(count)
