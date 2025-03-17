# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # diff parents && same depth >>> cousins
        node_x, node_y = [None, 0, False], [None, 0, False] # parent, depth, visited(find?)
        def wrap(node: Optional[TreeNode], parent: int, depth: int):
            if not node:
                return

            if node.val == x:
                node_x[0], node_x[1], node_x[2] = parent, depth, True

            if node.val == y:
                node_y[0], node_y[1], node_y[2] = parent, depth, True

            # if visited x, y
            if node_x[2] and node_y[2]:
                return

            wrap(node.left, node.val, depth + 1)
            wrap(node.right, node.val, depth + 1)


        wrap(root, None, 0)
        return (node_x[0] != node_y[0]) and (node_x[1] == node_y[1])

