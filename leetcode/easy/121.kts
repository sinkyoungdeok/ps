import kotlin.math.*

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var minValue = 1000000000
        var res = 0

        for (p in prices) {
            if (minValue != 1000000000 && p - minValue > 0) {
                res = max(res, p - minValue)
            }

            minValue = min(minValue, p)
        }

        return res
    }
}