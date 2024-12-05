import kotlin.math.*

class Solution {
    fun findMaxConsecutiveOnes(nums: IntArray): Int {
        var max = 0
        var sum = 0
        for (i in 0 until nums.size) {
            if (nums[i] != 0) {
                sum += nums[i]
            } else {
                max = max(sum, max)
                sum = 0
            }
        }

        return max(sum, max)
    }
}