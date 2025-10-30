n = int(input())
post_order = []
pre_order  = []
# pre_order_dict = {}
for i in range(1,n+1):
    num = int(input())
    pre_order.append(num)
    # pre_order_dict[num] = i


def build(left, right):
    if left > right:
        return
    
    #루트 값
    root = pre_order[left]

    #좌우 분리 root 보다 작거나 크거나
    idx = left + 1
    while idx < n and pre_order[idx] < root:
        idx += 1
    
    # if idx != left + 1:
    build(left+1, idx-1)
    # if idx <= n:
    build(idx, right)
    # post_order.append(root)
    print(root)

build(0,n-1)



