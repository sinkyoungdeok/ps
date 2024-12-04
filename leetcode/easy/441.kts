class Solution {
    fun arrangeCoins(n: Int): Int {
        var res = 0
        var num = n
        var base = 1

        while (num >= base) {
            num -= base
            res ++
            base ++
        }

        return res
    }
}