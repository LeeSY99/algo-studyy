# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}
        min_val = float('inf')
        max_val = float('-inf')

        def travel(node, row, col):
            nonlocal min_val, max_val
            if not node:
                return

            min_val = min(min_val, col)
            max_val = max(max_val, col)
            if col not in result:
                result[col] = [(row, node.val)]
            else:
                result[col].append((row, node.val))

            travel(node.left, row+1, col-1)
            travel(node.right, row+1, col+1)

        travel(root,0,0)
        print(result)
        print(min_val, max_val)
        ans = []
        for i in range(min_val, max_val+1):
            if i not in result:
                # print('i not in result')
                ans.append([])
            else:
                sub = []
                result[i].sort()
                for row, num in result[i]:
                    sub.append(num)
                ans.append(sub)
        return ans

        '''
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
        '''
        