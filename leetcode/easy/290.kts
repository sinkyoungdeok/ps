class Solution {
    fun wordPattern(pattern: String, s: String): Boolean {
        val ps = mutableMapOf<Char, String>()
        val sp = mutableMapOf<String, Char>()

        val splitData = s.split(" ")

        if (splitData.size != pattern.length) return false

        for (i in 0 until pattern.length) {
            val psData = ps.get(pattern[i])
            val spData = sp.get(splitData[i])

            if (psData == null && spData == null) {
                ps[pattern[i]] = splitData[i]
                sp[splitData[i]] = pattern[i]
                continue
            }

            if (psData != null && spData != null && psData == splitData[i]) {
                continue
            }

            return false
        }

        return true
    }
}