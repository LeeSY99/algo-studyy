n=int(input())
nums=list(map(int,input().split()))

def selection_sort(arr):
    for i in range(n-1):
        min_num=arr[i]
        min_index=i
        change=False
        for j in range(i+1,n):
            if arr[j]<min_num:
                min_index=j
                min_num=arr[j]
                change=True
        if change:
            arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

s_list=selection_sort(nums)
for e in s_list:
    print(e, end=' ')