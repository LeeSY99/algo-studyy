# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}
        nodes = []

        def travel(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            travel(node.left, row+1, col-1)
            travel(node.right, row+1, col+1)

        travel(root,0,0)
        
        nodes.sort()

        col_map = defaultdict(list)
        for col, row, val in nodes:
            col_map[col].append(val)

        result = []
        for col in sorted(col_map.keys()):
            result.append(col_map[col])

        return result