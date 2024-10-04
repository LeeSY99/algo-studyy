n=int(input())

nums=list(map(int,input().split()))

def radix_sort(arr):
    max_num=max(arr)
    
    exp=1
    while max_num//exp > 0:    
        arr_new=[]*10
        for i in range(n):
            index= (arr[i] // exp)%10
            arr_new[index].append(arr[i])

        store_arr=[]
        for i in range(10):
            for j in range(len(arr_new[i])):
                store_arr.append(arr_new[i][j])
    return store_arr

s_nums=radix_sort(nums)

for n in s_nums:
    print(n, end=' ')