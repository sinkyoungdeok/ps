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
    fun removeElements(head: ListNode?, `val`: Int): ListNode? {
        var curr = head
        var res = ListNode(-1)
        var resCurr = res

        while (curr != null) {
            if (curr.`val` != `val`) {
                resCurr.next = ListNode(curr.`val`)
                resCurr = resCurr.next
            }

            curr = curr.next
        }

        return res.next
    }
}