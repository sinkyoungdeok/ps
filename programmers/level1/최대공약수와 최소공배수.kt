import kotlin.math.*

class Solution {
    fun solution(n: Int, m: Int): IntArray {
        return intArrayOf(gcm(n, m), lcm(n, m))
    }

    fun gcm(a: Int, b: Int): Int {
        var maximum = max(a, b)
        var minimum = min(a, b)

        if (minimum == 0) {
            return maximum
        } else {
            return gcm(minimum, maximum % minimum)
        }
    }

    fun lcm(a: Int, b: Int): Int =
        (a * b) / gcm(a, b)
}