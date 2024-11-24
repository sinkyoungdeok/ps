class Solution {
    fun moveZeroes(nums: IntArray): Unit {
        var index = 0
        var zeroCnt = 0
        for (i in 0 until nums.size) {
            if (nums[i] == 0) {
                zeroCnt ++
                continue
            }

            nums[index++] = nums[i]
        }

        for (i in 0 until zeroCnt) {
            nums[nums.size - 1 - i] = 0
        }
    }
}