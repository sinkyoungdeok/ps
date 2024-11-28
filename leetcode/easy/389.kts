class Solution {
    fun findTheDifference(s: String, t: String): Char {
        val map = IntArray(27)
        for (c in s.toCharArray()) {
            map[c-'a']++
        }

        for (c in t.toCharArray()) {
            if (--map[c-'a'] == -1) return c
        }

        return 'a'
    }
}