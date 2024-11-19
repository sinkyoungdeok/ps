import java.util.*

class Solution {
    fun majorityElement(nums: IntArray): Int {
        val hashNum = HashMap<Int, Int>()

        nums.forEach {
            hashNum[it] = hashNum.getOrDefault(it, 0) + 1
        }

        return hashNum.toList().sortedByDescending { it.second }.let { it[0].first }
    }
}