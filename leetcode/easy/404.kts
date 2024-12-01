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
    var sum = 0

    fun sumOfLeftLeaves(root: TreeNode?): Int {
        if (root == null) return 0
        travel(root)
        return sum
    }

    fun travel(root: TreeNode) {
        root.left?.let {
            travel(root.left)
            if (haveChildren(root.left)) sum += root.left.`val`
        }
        root.right?.let {
            travel(root.right)
        }
    }

    fun haveChildren(root: TreeNode) = root.left == null && root.right == null
}