# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        prefixSum = {0:1}

        def dfs(node: Optional[TreeNode], currSum: int):
            if not node: return

            currSum += node.val
            self.count += prefixSum.get(currSum - targetSum, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1

            dfs(node.left, currSum)
            dfs(node.right, currSum)

            prefixSum[currSum] -= 1

        dfs(root, 0)
        return self.count