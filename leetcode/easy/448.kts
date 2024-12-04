class Solution {
    fun findDisappearedNumbers(nums: IntArray): List<Int> {
        var res = mutableSetOf<Int>()

        for (i in 1 until nums.size + 1) {
            res.add(i)
        }

        for (i in nums) {
            res.remove(i)
        }

        return res.toList()
    }
}