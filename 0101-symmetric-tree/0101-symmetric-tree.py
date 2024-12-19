# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            if not root.left and not root.right:
                return True

            return self.isMirror(root.left, root.right)

        def isMirror(self, l_node: Optional[TreeNode], r_node: Optional[TreeNode]) -> bool:
            if not l_node and not r_node:
                return True

            if not l_node or not r_node:
                return False

            if l_node.val != r_node.val:
                return False

            return self.isMirror(l_node.left, r_node.right) and self.isMirror(l_node.right, r_node.left)