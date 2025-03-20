# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         from collections import deque
#         q = deque([cloned])
#         while q:
#             curr_node = q.popleft()
#             if curr_node.val == target.val: return curr_node
#             if curr_node.left: q.append(curr_node.left)
#             if curr_node.right: q.append(curr_node.right)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [cloned]
        while queue:
            curr_node = queue[0]
            del queue[0]
            if curr_node.val == target.val: return curr_node
            if curr_node.left: queue.append(curr_node.left)
            if curr_node.right: queue.append(curr_node.right)