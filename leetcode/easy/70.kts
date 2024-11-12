class Solution {
    fun climbStairs(n: Int): Int {
        val nums = MutableList(46) { 0 }

        nums[1] = 1
        nums[2] = 2

        for (i in 3 until 45) {
            nums[i] = nums[i-1] + nums[i-2]
        }

        return nums[n]
    }
}