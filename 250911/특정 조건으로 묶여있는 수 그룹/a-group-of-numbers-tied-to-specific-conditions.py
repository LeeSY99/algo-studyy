n,k = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()
# print(arr)
L = [0] * n
R = [0] * n

i = 0
max_num = 0
#L[i] = 1~i번 숫자들 중 조건만족 그룹 딱 하나 만든다고 하면 가장 많은 숫자 개수
for j in range(n):
    while i < n and arr[j] - arr[i] > k:
        i+=1
    max_num = max(max_num, j-i+1)
    L[j] = max_num

max_num = 0
j = n-1
#R[i] = i~n번까지 숫자 중 조건만족 그룹 딱 하나 만든다고 하면 가장 많은 숫자 개수
for i in range(n-1,-1,-1):
    while j > i and arr[j] - arr[i] > k:
        j-=1
    
    max_num = max(max_num, j-i+1)
    R[i] = max_num

ans = L[n-1]
# print(arr)
# print(L)
# print(R)

for i in range(1,n-1):
    ans = max(ans, L[i] + R[i+1])

print(ans)