/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun minDepth(root: TreeNode?): Int {
        if (root == null) return 0

        return minDepth(root, 1)
    }

    fun minDepth(root: TreeNode?, depth: Int): Int{
        if (root == null) {
            return depth
        }

        if (root.left == null && root.right == null) {
            return depth
        }

        var leftDepth = 10000000
        var rightDepth = 10000000
        if (root.left != null) {
            leftDepth = minDepth(root.left, depth + 1)
        }

        if (root.right != null) {
            rightDepth = minDepth(root.right, depth + 1)
        }

        if (leftDepth > rightDepth) return rightDepth
        else return leftDepth
    }
}