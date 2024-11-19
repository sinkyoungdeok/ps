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
    fun countNodes(root: TreeNode?): Int {
        return traversal(root)
    }

    fun traversal(root: TreeNode?): Int {
        if (root == null) return 0

        var sum = 1

        if (root.left != null) {
            sum += traversal(root.left)
        }

        if (root.right != null) {
            sum += traversal(root.right)
        }

        return sum
    }
}