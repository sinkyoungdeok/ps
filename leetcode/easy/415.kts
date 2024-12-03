class Solution {
    fun addStrings(num1: String, num2: String): String {
        var carry = 0
        var res = ""

        var i1 = num1.length - 1
        var i2 = num2.length - 1

        while(i1 >= 0 && i2 >= 0) {
            var temp = Character.getNumericValue(num1[i1]) + Character.getNumericValue(num2[i2]) + carry

            res += temp % 10
            carry = temp / 10

            i1 --
            i2 --
        }

        for (i in i1 downTo 0) {
            var temp = Character.getNumericValue(num1[i]) + carry

            res += temp % 10
            carry = temp / 10
        }

        for (i in i2 downTo 0) {
            var temp = Character.getNumericValue(num2[i]) + carry

            res += temp % 10
            carry = temp / 10
        }

        if (carry > 0) {
            res += carry.toString()
        }

        return res.reversed()
    }
}