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

function isBalanced(root: TreeNode | null): boolean {
    if (!root) return true

    const leftNodeMaxDepth = getMaxDepth(root.left)
    const rightNodeMaxDepth = getMaxDepth(root.right)

    if ((Math.abs(leftNodeMaxDepth - rightNodeMaxDepth)) > 1) return false

    return isBalanced(root.left) && isBalanced(root.right)
};

function getMaxDepth(root: TreeNode | null): number {
    return !root ? 0 : (Math.max(getMaxDepth(root.left), getMaxDepth(root.right))) + 1
}