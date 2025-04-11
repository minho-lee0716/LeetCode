# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def calculateCount(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            count = 1 if current_sum == targetSum else 0
            count += calculateCount(node.left, current_sum)
            count += calculateCount(node.right, current_sum)
            return count
        
        def dfs(node):
            if not node:
                return 0
            
            count = calculateCount(node, 0)
            count += dfs(node.left)
            count += dfs(node.right)
            return count
        
        return dfs(root)