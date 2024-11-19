import java.util.*

class Solution {
    fun containsNearbyDuplicate(nums: IntArray, k: Int): Boolean {
        val map = mutableMapOf<Int, Int>()

        nums.forEachIndexed { i, v ->
            if (map.get(v) != null && i - map.get(v)!! <= k) {
                return true
            }

            map[v] = i
        }

        return false
    }
}