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
    fun inorderTraversal(root: TreeNode?): List<Int> {
        if (root == null) {
            return emptyList()
        }
        val answer = mutableListOf<Int>()
        inorderTraversal(root, answer)
        return answer
    }

    private fun inorderTraversal(root: TreeNode?, answer: MutableList<Int>) {
        if (root == null) {
            return
        }

        if (root.left != null) {
            inorderTraversal(root.left, answer)
        }
        answer.add(root.`val`)
        if (root.right != null) {
            inorderTraversal(root.right, answer)
        }
    }
}