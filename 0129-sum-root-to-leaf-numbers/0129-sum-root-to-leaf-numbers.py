# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        nodes = []
        
        def backtrack(node):
            nonlocal ans
            nodes.append(node)
            if node.left == None and node.right == None:
                ans += calc()
                return

            if node.left:
                backtrack(node.left)
                nodes.pop()
            if node.right:
                backtrack(node.right)
                nodes.pop()

        def calc():
            num_sum = 0
            for i in range(len(nodes)):
                num_sum += nodes[len(nodes) - i - 1].val * (10**i)
            print(num_sum)
            return num_sum
        backtrack(root)
        return ans
                
        

