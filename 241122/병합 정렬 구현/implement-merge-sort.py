n=int(input())

nums = list(map(int,input().split()))

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

def merge(left,right):
    merged=[]
    i ,j= 0, 0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1

    #남아 있을 수 있음
    for l in range(i,len(left)):
        merged.append(left[l])

    for l in range(j,len(right)):
        merged.append(right[l])
    
    return merged

after_sort=merge_sort(nums)
for num in after_sort:
    print(num, end=' ')