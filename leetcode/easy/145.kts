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
    fun postorderTraversal(root: TreeNode?): List<Int> {
        val ans = mutableListOf<Int>()
        postorderTraversal(root, ans)
        return ans
    }

    fun postorderTraversal(root: TreeNode?, ans: MutableList<Int>) {
        if(root == null) {
            return
        }

        if (root.left != null) {
            postorderTraversal(root.left, ans)
        }

        if (root.right != null) {
            postorderTraversal(root.right, ans)
        }

        ans.add(root.`val`)
    }
}