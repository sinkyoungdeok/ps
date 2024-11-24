class Solution {
    fun isPowerOfTwo(n: Int): Boolean {
        if (n <= 0) return false

        var res = 1

        for (i in 0 until 32) {
            if (res == n) return true
            res *= 2
        }

        return false
    }
}