n = int(input())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, n):
    if arr[i-1] == 0:
        cnt += 1
        arr[i-1] = 1
        if arr[i] == 1:
            arr[i] = 0
        else:
            arr[i] = 1
        
        if arr[i+1] == 1:
            arr[i+1] = 0
        else:
            arr[i+1] = 1

print(cnt)