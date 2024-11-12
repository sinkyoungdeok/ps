/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun deleteDuplicates(head: ListNode?): ListNode? {
        val start = head
        var curr = head
        var tempNode = head ?: ListNode(-200)
        curr = curr?.next

        while (curr != null) {
            if (tempNode.`val` == curr.`val`) {
                if (curr.next == null) {
                    tempNode.next = null
                }
                curr = curr.next
                continue
            } else {
                val next = curr.next
                tempNode.next = curr
                tempNode = curr
                curr = next
            }
        }

        return start
    }
}