class Solution {
    fun isSubsequence(s: String, t: String): Boolean {
        if (s.length == 0) return true

        var si = 0

        for (i in 0 until t.length) {
            if (t[i] == s[si]) {
                si += 1

                if (si == s.length) return true
            }
        }

        return si == s.length
    }
}