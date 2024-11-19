class Solution {
    fun convertToTitle(columnNumber: Int): String {
        var number = columnNumber
        var res = ""

        while (number > 0) {
            res += ('A' + (number - 1) % 26)
            number = (number - 1) / 26
        }

        return res.reversed().toString()
    }
}