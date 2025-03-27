# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = 10 ** 5 # 0 <= Node.val <= 105
        self.prev_val = None

        def inorderTraversal(root: Optional[TreeNode]):
            if not root:
                return

            inorderTraversal(root.left)
            
            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, root.val - self.prev_val)

            self.prev_val = root.val
            inorderTraversal(root.right)

        inorderTraversal(root)
        return self.min_diff