k = int(input())
in_res = list(map(int, input().split()))
tree = [0] * (2**k)


def inorder(x):
    if x > 2**k -1:
        return
    inorder(x*2)
    setting(x)
    inorder(x*2+1)
idx = 0
def setting(x):
    global idx
    tree[x] = in_res[idx]
    idx += 1

inorder(1)
# print(tree)

height = 1
idx = 1
while height<=k:
    for _ in range(2**(height-1)):
        print(tree[idx], end = ' ')
        idx += 1
    print()
    height += 1


    


