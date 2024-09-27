n=int(input())
nums=list(map(int,input().split()))

def bubble_sort(arr):
    sorted=False
    while(sorted==False):
        for j in range(n):
            for i in range(n-1):
                sorted=True
                if arr[i]>arr[i+1]:
                    arr[i],arr[i+1]=arr[i+1],arr[i]
                    sorted=False
    return arr

s_list=bubble_sort(nums)
for e in s_list:
    print(e, end=' ')