n=int(input())
nums = list(map(int,input().split()))

def heapify(arr,n,i):
    '''n 힙 크기, i 인덱스'''
    largest=i #루트를 가장 큰 값으로
    left = 2*i+1 #왼쪽 자식
    right = 2*i+2 #오른쪽 자식

    if left < n and arr[left]>arr[largest]: 
        largest=left 
    
    if right < n and arr[right]>arr[largest]:
        largest=right

    #max가 루트가 아니면 교환
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    for i in range(n//2-1 , -1, -1):
        heapify(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


heap_sort(nums)
print(*nums)