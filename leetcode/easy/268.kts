class Solution {
    fun missingNumber(nums: IntArray): Int {
        nums.sort()
        for (i in 0 until nums.size) {
            if (i != nums[i]) return i
        }

        return nums.size
    }
}