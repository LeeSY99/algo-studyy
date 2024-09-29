n=int(input())
nums=list(map(int,input().split()))

def insert_sort(arr):
    for i in range(1,n):
        j=i-1
        key=arr[i]
        while(j>=0 and (arr[j] > key)):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr

s_list=insert_sort(nums)
for e in s_list:
    print(e,end=' ')