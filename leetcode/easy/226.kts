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
    fun invertTree(root: TreeNode?): TreeNode? {
        return invertTrees(root)
    }

    fun invertTrees(root: TreeNode?): TreeNode? {
        if (root == null) {
            return null
        }

        val left = root.left
        val right = root.right

        root.left = right
        root.right = left

        if (left != null) {
            invertTrees(left)
        }

        if (right != null) {
            invertTrees(right)
        }

        return root
    }
}