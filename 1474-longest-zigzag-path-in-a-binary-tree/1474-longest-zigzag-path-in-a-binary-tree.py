# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.maxZigzagLength = 0
        
        def dfs(node: Optional[TreeNode], move: str, currLength: int):
            if not node:
                return

            self.maxZigzagLength = max(self.maxZigzagLength, currLength)

            if move == 'L':
                dfs(node.right, 'R', currLength + 1)
                dfs(node.left, 'L', 1)

            elif move == 'R':
                dfs(node.left, 'L', currLength + 1)
                dfs(node.right, 'R', 1)

        dfs(root.left, 'L', 1)
        dfs(root.right, 'R', 1)
        return self.maxZigzagLength