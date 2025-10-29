n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
import sys
sys.setrecursionlimit(100000)
in_order_map = {}
for i in range(n):
    in_order_map[in_order[i]] = i 

pre_order = [0] * n
idx = 0

def build(in_l, in_r, po_l, po_r):
    global idx
    if po_l > po_r:
        return
    
    root = post_order[po_r]
    mid = in_order_map[root]

    left_size = mid - in_l
    right_size = in_r - mid

    pre_order[idx] = root
    idx += 1
    build(in_l, mid-1, po_l, po_l + left_size-1)
    build(mid+1, in_r, po_l + left_size, po_r-1)
    

build(0,n-1,0,n-1)
print(*pre_order)

