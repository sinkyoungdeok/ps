import java.util.*

class Solution {
    fun isIsomorphic(s: String, t: String): Boolean {
        val sMap = HashMap<Char, Char>()
        val tMap = HashMap<Char, Char>()

        for (i in 0 until s.length) {
            if (sMap.get(s[i]) == null && tMap.get(t[i]) == null) {
                sMap[s[i]] = t[i]
                tMap[t[i]] = s[i]

                continue
            }

            if (sMap.get(s[i]) != null && tMap.get(t[i]) != null) {
                if (sMap.get(s[i]) == t[i]) {
                    continue
                } else {
                    return false
                }

                continue
            }

            return false
        }

        return true
    }
}