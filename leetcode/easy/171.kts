class Solution {
    fun titleToNumber(columnTitle: String): Int {
        var res = 0
        var reversedTitle = columnTitle.reversed()
        var base = 1

        for (s in reversedTitle) {
            res += (s - 'A' + 1) * base
            base *= 26
        }

        return res
    }
}