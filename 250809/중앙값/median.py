import heapq
t = int(input())


def add_number(num):
    #왼족이 비었거나 왼쪽 최대값보다 작거나 같으면
    if not left or num <= -left[0]:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right,num)

    #2) 균형 왼쪽이 더 많아야함
    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))
    elif len(right) > len(left):
        heapq.heappush(left, -heapq.heappop(right))

def get_median():
    return -left[0]



for _ in range(t):
    m = int(input())
    nums = list(map(int, input().split()))
    left = [] #최대 힙
    right = []
    
    for i, num in enumerate(nums,1):
        add_number(num)
        if i%2 == 1:
            print(get_median(), end = ' ')
    print()



