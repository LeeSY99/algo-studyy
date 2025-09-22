n = int(input())
B = list(int(input()) for _ in range(n))
B.sort()
j = 0
A = []
for i in range(1,2*n+1):
    if j < n and i == B[j]:
        j+=1
        continue
    else:
        A.append(i)

j = 0
score = 0
for a in A:
    if j < n and a > B[j]:
        score += 1
        j+=1
print(score)
        
        
