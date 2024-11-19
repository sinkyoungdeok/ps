import java.util.*

class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val set = mutableSetOf<Int>()
        nums.forEach {
            if (set.contains(it)) return true
            set.add(it)
        }

        return false
    }
}