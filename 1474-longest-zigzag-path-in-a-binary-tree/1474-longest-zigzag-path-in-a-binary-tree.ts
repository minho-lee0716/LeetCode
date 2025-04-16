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

function longestZigZag(root: TreeNode | null): number {
    let maxZigzagLength = 0

    const dfs = (node: TreeNode | null, move: string, currLength: number) => {
        if (!node) return

        maxZigzagLength = Math.max(maxZigzagLength, currLength)

        if (move === 'L') {
            dfs(node.right, 'R', currLength + 1)
            dfs(node.left, 'L', 1)
        }

        else if (move === 'R') {
            dfs(node.left, 'L', currLength + 1)
            dfs(node.right, 'R', 1)
        }
    }

    dfs(root.left, 'L', 1)
    dfs(root.right, 'R', 1)
    return maxZigzagLength
};