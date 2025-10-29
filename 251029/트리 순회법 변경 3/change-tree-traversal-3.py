n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_order_map = {}
for i in range(n):
    in_order_map[in_order[i]] = i 


post_idx = n-1

def build(in_l, in_r):
    global post_idx
    if in_l > in_r:
        return []
    
    root = post_order[post_idx]
    post_idx -= 1

    mid = in_order_map[root]

    right_pre = build(mid+1, in_r)
    left_pre = build(in_l, mid-1)
    return [root] + left_pre + right_pre

pre_order = build(0,n-1)
print(*pre_order)

