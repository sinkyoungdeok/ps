class Solution {
    fun searchInsert(nums: IntArray, target: Int): Int {
        var start = 0
        var end = nums.size

        while(start < end) {
            val mid = (start + end) / 2

            if (nums[mid] > target) {
                end = mid
            } else if(nums[mid] < target) {
                start = mid + 1
            } else {
                return mid
            }
        }

        return start
    }
}

println(Solution().searchInsert(intArrayOf(1,3,5,6), 7)) // 2