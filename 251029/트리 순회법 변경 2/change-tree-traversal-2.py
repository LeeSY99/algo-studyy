n = int(input())
pre_res = list(map(int, input().split()))
in_res = list(map(int, input().split()))

post_res = [0] * n 
in_order_map = {}
for i in range(n):
    in_order_map[in_res[i]] = i

cnt = 0
def build(pr_l, pr_r, in_l, in_r):
    global cnt
    if pr_l > pr_r:
        return

    root = pre_res[pr_l]
    mid = in_order_map[root]

    left_size = mid - in_l
    right_size = in_r - mid

    build(pr_l+1, pr_l+left_size, in_l, mid - 1)
    build(pr_l+left_size + 1, pr_r, mid + 1, in_r)
    
    post_res[cnt] = root
    cnt += 1
    

build(0,n-1,0,n-1)
print(*post_res)