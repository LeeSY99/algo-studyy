n,m = map(int, input().split())

nums = list(map(int, input().split()))

#x이상이 처음 나오는 위치
def lower_bound(x):
    left, right = 0, n-1
    index = n
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            index = min(index, mid)
    return index
        
#x초과가 처음 나오는 위치
def upper_bound(x):
    left, right = 0, n-1
    index = n
    while left<=right:
        mid = (left+right)//2
        if nums[mid] <= x:
            left= mid +1
        else:
            right = mid -1 
            index = min(index,mid)
    return index

for _ in range(m):
    a = int(input())
    print(upper_bound(a) - lower_bound(a))