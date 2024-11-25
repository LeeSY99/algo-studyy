n=int(input())

nums = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:len(arr)-1] if x<= pivot]
    right = [x for x in arr[:len(arr)-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

sorted_nums = quick_sort(nums)
print(*sorted_nums)