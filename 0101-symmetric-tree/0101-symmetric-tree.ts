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

function isSymmetric(root: TreeNode | null): boolean {
    if (!root.left && !root.right) return true;
    return isMirror(root.left, root.right);
};

function isMirror(leftNode: TreeNode | null, rightNode: TreeNode | null): boolean {
    if (!leftNode && !rightNode) return true;
    if (!leftNode || !rightNode) return false;
    if (leftNode.val !== rightNode.val) return false;
    return isMirror(leftNode.left, rightNode.right) && isMirror(leftNode.right, rightNode.left);
}