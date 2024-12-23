/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;

        int leftNodeMaxDepth = getMaxDepth(root.left);
        int rightNodeMaxDepth = getMaxDepth(root.right);

        if (Math.abs(leftNodeMaxDepth - rightNodeMaxDepth) > 1) return false;

        return isBalanced(root.left) && isBalanced(root.right);
    }

    private int getMaxDepth(TreeNode node) {
        if (node == null) return 0;

        if (node.left == null && node.right == null) return 1;

        return Math.max(getMaxDepth(node.left), getMaxDepth(node.right)) + 1;
    }
}