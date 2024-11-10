class Solution {
    fun isPalindrome(x: Int): Boolean {
        val str = x.toString()
        val reverseStr = x.toString().reversed()

        return str == reverseStr
    }
}