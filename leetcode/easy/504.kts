import kotlin.math.*

class Solution {
    fun convertToBase7(num: Int): String {
        var n = num
        var res = ""

        while(n != 0) {
            res += abs((n % 7)).toString()
            n /= 7
        }

        if (num < 0) {
            return "-" + res.reversed()
        } else if (num ==0 ) {
            return "0"
        }

        return res.reversed()
    }
}