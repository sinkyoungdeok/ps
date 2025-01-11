class Solution {
    fun findComplement(num: Int): Int {
        var binaryNum = ""
        var n = num

        while(n > 0) {
            binaryNum += n % 2
            n /= 2
        }

        var complementNum = ""
        for (i in binaryNum) {
            complementNum += (Character.getNumericValue(i) xor 1).toString()
        }

        var res = 0
        var base = 1
        for (i in complementNum) {
            res += Character.getNumericValue(i) * base
            base *= 2
        }

        return res
    }
}