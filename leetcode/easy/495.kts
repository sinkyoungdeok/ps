class Solution {
    fun findPoisonedDuration(timeSeries: IntArray, duration: Int): Int {
        var res = 0
        var curr = 0

        for (i in timeSeries) {
            res += duration
            if (curr > i) {
                res -= (curr - i)
            }
            curr = duration + i
        }

        return res
    }
}