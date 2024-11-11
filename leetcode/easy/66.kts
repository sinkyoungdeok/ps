class Solution {
    fun plusOne(digits: IntArray): IntArray {
        digits[digits.size-1] += 1

        var carry = 0
        for (i in digits.size-1 downTo 0) {
            digits[i] += carry
            carry = 0
            if (digits[i] == 10) {
                carry = 1
                digits[i] = 0
            }
        }

        if(carry == 1) {
            return intArrayOf(1) + digits
        }

        return digits
    }
}