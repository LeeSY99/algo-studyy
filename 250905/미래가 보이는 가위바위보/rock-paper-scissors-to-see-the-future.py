n = int(input())
H = 0
S = 1
P = 2

B = [input() for _ in range(n)]
for i in range(n):
    if B[i] == 'H':
        B[i] = H
    elif B[i] == 'S':
        B[i] = S
    else:
        B[i] = P
L = [[0]*n for _ in range(3)] 

R = [[0]*n for _ in range(3)] 

for i in range(n):
    if B[i] == H:
        L[2][i] += 1
    elif B[i] == S:
        L[0][i] += 1
    else:
        L[1][i] += 1

    if i>0:
        for j in range(3):
            L[j][i] += L[j][i-1]  

for i in range(n-1,-1,-1):
    if B[i] == H:
        R[2][i] += 1
    elif B[i] == S:
        R[0][i] += 1
    else:
        R[1][i] += 1
    if i < n-1:
        for j in range(3):
            R[j][i] += R[j][i+1]     

ans = 0
for i in range(1,n-1):
    for j in range(3):
        for k in range(3): ## i번쨰 위치까지 j 다음 k로 바꿈
            # if i == j : continue
            # if B[i] == k: 
            #     val = 1 
            # else: 
            #     val = 0
            ans = max(ans, L[j][i] + R[k][i+1])

# for l in L:
#     print(*l)
# print()
# for r in R:
#     print(*r)
print(ans)


    