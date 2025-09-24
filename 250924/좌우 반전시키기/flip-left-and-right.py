n = int(input())
arr = list(map(int, input().split()))

def in_range(i):
    return 1<=i<n
cnt = 0
for i in range(1, n):
    if arr[i-1] == 0:
        cnt += 1
        arr[i-1] = 1
        if arr[i] == 1:
            arr[i] = 0
        else:
            arr[i] = 1
        
        if in_range(i+1) and arr[i+1] == 1:
            arr[i+1] = 0
        elif in_range(i+1) and arr[i+1]==0:
            arr[i+1] = 1

if sum(arr) != n:
    cnt = -1
print(cnt)