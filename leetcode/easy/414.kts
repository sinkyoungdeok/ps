class Solution {
    fun thirdMax(nums: IntArray): Int {
        val res = nums.toSet().toList().sorted()

        if (res.size >= 3) {
            return res[res.size - 3]
        } else {
            return res.max()
        }
    }
}