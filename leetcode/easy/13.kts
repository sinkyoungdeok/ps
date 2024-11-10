class Solution {
    fun romanToInt(s: String): Int {
        val map = mapOf(
            'I' to 1,
            'V' to 5,
            'X' to 10,
            'L' to 50,
            'C' to 100,
            'D' to 500,
            'M' to 1000,
        )
        var sum = 0
        for (i in 0..s.length-1) {
            sum += map[s[i]] ?: 0

            if (i == 0) continue

            val prev = map[s[i-1]] ?: 0
            val curr = map[s[i]] ?: 0
            if (prev < curr) {
                sum -= prev * 2
            }
        }

        return sum
    }
}