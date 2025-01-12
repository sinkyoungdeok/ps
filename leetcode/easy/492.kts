class Solution {
    fun constructRectangle(area: Int): IntArray {
        var L = area
        var W = 1

        for (i in 2 until area + 1 / 2) {
            if (area % i != 0) continue
            if (area / i < i) continue

            L = area / i
            W = i
        }

        return mutableListOf(L, W).toIntArray()
    }
}