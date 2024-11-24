class Solution {
    fun isPowerOfThree(n: Int): Boolean {
        if (n <= 0) return false

        var res = 1

        for (i in 0 until 30) {
            if (n == res) return true
            res *= 3
        }

        return false
    }
}