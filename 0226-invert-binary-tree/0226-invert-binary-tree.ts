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

function invertTree(root: TreeNode | null): TreeNode | null {
    return switchTree(root);  
};

function switchTree(root: TreeNode | null): TreeNode | null {
    if (!root) {
      return null;
    }

    const tmp = switchTree(root.right);
    root.right = switchTree(root.left);
    root.left = tmp;

    return root;
};