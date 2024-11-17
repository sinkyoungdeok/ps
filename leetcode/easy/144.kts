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
    fun preorderTraversal(root: TreeNode?): List<Int> {
        val ans = mutableListOf<Int>()
        preorderTraversal(root, ans)
        return ans
    }

    fun preorderTraversal(root: TreeNode?, ans: MutableList<Int>) {
        if(root == null) {
            return
        }

        ans.add(root.`val`)
        if (root.left != null) {
            preorderTraversal(root.left, ans)
        }

        if (root.right != null) {
            preorderTraversal(root.right, ans)
        }
    }
}