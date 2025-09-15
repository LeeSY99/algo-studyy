n,m = map(int, input().split())
pos = list(map(int, input().split()))
lines = [tuple(map(int, input().split())) for _ in range(m)]

def lower_bound(x):
    left = 0
    right = n-1
    idx = n

    while left <= right:
        mid = (left + right) // 2
        if pos[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            idx = min(idx, mid)

    return idx

def upper_bound(x):
    left = 0
    right = n-1
    idx = n

    while left <= right:
        mid = (left + right) // 2
        if pos[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
            idx = min(idx, mid)
    return idx


for x1, x2 in lines:
    print(upper_bound(x2) - lower_bound(x1) )

