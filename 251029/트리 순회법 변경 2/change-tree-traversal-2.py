n = int(input())
pre_res = list(map(int, input().split()))
in_res = list(map(int, input().split()))

post_res = []
in_order_map = {}
for i in range(n):
    in_order_map[in_res[i]] = i

pre_idx = 0
def build(in_l, in_r):
    global pre_idx
    if in_l > in_r:
        return

    root = pre_res[pre_idx]
    pre_idx += 1

    mid = in_order_map[root]
    build(in_l, mid-1)
    build(mid+1, in_r)
    post_res.append(root)

build(0,n-1)
print(*post_res)