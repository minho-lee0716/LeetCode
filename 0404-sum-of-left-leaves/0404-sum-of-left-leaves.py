# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def getLeftLeaveVal(root: Optional[TreeNode], isLeft: bool) -> int:
            if not root:
                return 0

            if not root.left and not root.right and isLeft:
                return root.val

            return getLeftLeaveVal(root.left, True) + getLeftLeaveVal(root.right, False)

        return getLeftLeaveVal(root, False)