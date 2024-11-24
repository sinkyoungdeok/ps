class NumArray(nums: IntArray) {
    val dp = IntArray(nums.size+1)

    init {
        for (i in 1 until nums.size + 1) {
            dp[i] = dp[i-1] + nums[i-1]
        }
    }

    fun sumRange(left: Int, right: Int): Int {
        return dp[right+1]-dp[left]
    }

}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */