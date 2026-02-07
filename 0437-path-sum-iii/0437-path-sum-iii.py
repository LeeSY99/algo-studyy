# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = 0

        def dfs(node, cur):
            nonlocal ans
            if not node:
                return

            cur += node.val
            ans += prefix[cur - targetSum]

            prefix[cur] += 1
            dfs(node.left, cur)
            dfs(node.right, cur)
            prefix[cur] -= 1

        dfs(root, 0)
        return ans

        