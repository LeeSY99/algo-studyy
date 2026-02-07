# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        if not root:
            return ans

        def calc(node, now_sum):
            if not node:
                return 0
            now_sum += node.val
            res = 0
            if now_sum == targetSum:
                res = 1
            res += calc(node.left, now_sum)
            res += calc(node.right, now_sum)
            return res

        def dfs(node):
            if not node:
                return 0
            return calc(node,0) + dfs(node.left) + dfs(node.right)

        return dfs(root)

        