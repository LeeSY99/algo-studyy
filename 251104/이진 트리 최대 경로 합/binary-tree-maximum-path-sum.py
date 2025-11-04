n = int(input())


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.left = None
        self.right = None
nodes = [None] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    node = nodes[a]
    if node == None:
        node = Node(a)
        nodes[a] = node
    
    b_node = Node(b)
    nodes[b] = b_node
    if node.left == None:
        node.left = b_node
    else:
        node.right = b_node

nums = [0]
for _ in range(n):
    nums.append(int(input()))

ans = 0
def get_path(root):
    global ans
    if root == None:
        return 0

    left_path = get_path(root.left)
    right_path = get_path(root.right)

    one_part_max = max(nums[root.idx] + left_path, nums[root.idx] + right_path)
    two_part_max = nums[root.idx] + left_path + right_path
    ans = max(ans, one_part_max, two_part_max)

    return max(one_part_max, 0)
# print(nodes)
get_path(nodes[1])
print(ans)


