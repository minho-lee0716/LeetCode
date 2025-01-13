/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumOfLeftLeaves(root: TreeNode | null): number {
    const getLeftLeaveVal = (node: TreeNode | null, isLeft: boolean): number => {
      if (!node) {
        return 0;
      }

      if (!node.left && !node.right && isLeft) {
        return node.val;
      }

      return getLeftLeaveVal(node.left, true) + getLeftLeaveVal(node.right, false);
    };

    return getLeftLeaveVal(root, false);
};