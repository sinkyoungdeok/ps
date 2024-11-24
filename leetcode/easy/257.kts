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
    fun binaryTreePaths(root: TreeNode?): List<String> {
        if (root == null) return listOf()

        val answer = mutableListOf<String>()

        binaryTreePaths(root, answer, mutableListOf<Int>())

        return answer
    }

    fun binaryTreePaths(root: TreeNode?, answer: MutableList<String>, temp: MutableList<Int>) {
        if (root == null) return

        temp.add(root.`val`)
        if (root.left == null && root.right == null) {
            answer.add(temp.joinToString("->"))

            return
        }

        if (root.left != null) {
            binaryTreePaths(root.left, answer, temp)
            temp.removeAt(temp.size-1)
        }

        if (root.right != null) {
            binaryTreePaths(root.right, answer, temp)
            temp.removeAt(temp.size-1)
        }
    }
}