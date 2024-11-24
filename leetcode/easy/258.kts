class Solution {
    fun addDigits(num: Int): Int {
        var res = num

        while (res >= 10) {
            var temp = res
            res = 0

            while(temp >= 1) {
                res += temp % 10
                temp /= 10
            }
        }

        return res
    }
}