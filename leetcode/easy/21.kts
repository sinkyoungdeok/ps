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
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var list1cp = list1
        var list2cp = list2
        var dHead = ListNode(0)
        var curr = dHead

        while(list1cp != null && list2cp != null) {
            if (list1cp.`val` < list2cp.`val`) {
                curr.next = list1cp
                list1cp = list1cp.next
            } else {
                curr.next = list2cp
                list2cp = list2cp.next
            }

            curr = curr.next
        }

        if(list1cp == null) curr.next = list2cp
        if(list2cp == null) curr.next = list1cp

        return dHead.next
    }
}