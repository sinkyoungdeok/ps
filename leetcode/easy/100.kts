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
    fun isSameTree(p: TreeNode?, q: TreeNode?): Boolean {
        return inorderTraversal(p, q)
    }

    private fun inorderTraversal(p: TreeNode?, q: TreeNode?): Boolean {
        if(p == null && q == null) return true

        if(p == null || q == null) return false

        if(p.`val` != q.`val`) return false

        if(p.left != null || q.left != null) {
            if(inorderTraversal(p.left, q.left) == false) {
                return false
            }
        }

        if(p.right != null || q.right != null) {
            if(inorderTraversal(p.right, q.right) == false) {
                return false
            }
        }

        return true
    }
}