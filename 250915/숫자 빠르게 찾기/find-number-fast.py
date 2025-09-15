n,m  = map(int, input().split())

nums = list(map(int, input().split()))


def search(a):
    left = 0
    right = n-1
    while left<=right:
        mid = (left+right) // 2
        if nums[mid] > a:
            right = mid-1
        elif nums[mid] < a:
            left = mid + 1
    
        elif nums[mid] == a:
            return mid+1
    return -1
    



for _ in range(m):
    a = int(input())
    print(search(a))
        