import kotlin.math.*

class Solution {
    fun plusOne(digits: IntArray): IntArray {
        var sum = 1
        digits.forEachIndexed { idx, digit ->
            sum += digit * (10.0).pow(digits.size-1-idx).toInt()
        }

        return sum.toString().toCharArray().map { it.toString().toInt() }.toIntArray()
    }
}