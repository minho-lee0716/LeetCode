# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftNodeMaxDepth = self.getMaxDepth(root.left)
        rightNodeMaxDepth = self.getMaxDepth(root.right)

        if abs(leftNodeMaxDepth - rightNodeMaxDepth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getMaxDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        if not node.left and not node.right:
            return 1

        return max(self.getMaxDepth(node.left) + 1, self.getMaxDepth(node.right) + 1)
        