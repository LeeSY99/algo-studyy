n, k = map(int, input().split())

arr = list(map(int, input().split()))
count = {}

def can_go(j):
    if arr[j] not in count:
        return True
    if count[arr[j]] < k:
        return True
    return False

j = 0
ans = 0
for i in range(n):
    while j<n and can_go(j):
        if arr[j] not in count:
            count[arr[j]] = 1
        else:
            count[arr[j]] += 1
        
        j += 1

    ans = max(ans, j-i)
    count[arr[i]] -= 1

print(ans)


