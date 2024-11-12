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
    fun isSymmetric(root: TreeNode?): Boolean {
        if (root == null) return true

        return inorderTraversal(root.left, root.right)
    }

    private fun inorderTraversal(r: TreeNode?, l: TreeNode?): Boolean {
        if (r == null && l == null) return true

        if (r == null || l == null) return false

        if (r.`val` != l.`val`) return false

        if (r.left != null || l.right != null) {
            if(inorderTraversal(r.left, l.right) == false) {
                return false
            }
        }

        if (r.right != null || l.left != null) {
            if(inorderTraversal(r.right, l.left) == false) {
                return false
            }
        }

        return true
    }
}