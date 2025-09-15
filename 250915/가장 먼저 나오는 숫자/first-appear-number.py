n,m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

def lower_bound(a):
    left = 0
    right = n-1
    index = n

    while left<=right:
        mid = (left + right) // 2
        if arr[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
            if arr[mid] == a:
                index = min(index, mid)
    return index

for q in query:
    res = lower_bound(q)
    if res == n:
        print(-1)
    else:
        print(res+1)

