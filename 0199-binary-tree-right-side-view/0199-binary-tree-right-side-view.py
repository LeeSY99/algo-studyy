# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        def find(node, depth):
            if depth > len(result):
                result.append(node.val)
            if node.right:
                find(node.right, depth + 1)
            if node.left:
                find(node.left, depth + 1)
        
        find(root,1)
        return result
            
        