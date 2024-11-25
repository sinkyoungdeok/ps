class Solution {
    fun isPerfectSquare(num: Int): Boolean {
        for (i in 1 until 50000) {
            if (i * i == num) return true
        }

        return false
    }
}