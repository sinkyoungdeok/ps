class Solution {
    fun removeElement(nums: IntArray, `val`: Int): Int {
        var numIndex = 0
        for (num in nums) {
            if (num != `val`) {
                nums[numIndex++] = num
            }
        }

        return numIndex
    }
}