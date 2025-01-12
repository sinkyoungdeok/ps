class Solution {
    fun licenseKeyFormatting(s: String, k: Int): String {
        val removeDashStr = s.replace("-", "").toMutableList()

        if (removeDashStr.size == 0) {
            return ""
        }

        val firstLength = removeDashStr.size % k
        var res = ""

        for (i in 0 until firstLength) {
            res += removeDashStr[0].toUpperCase()
            removeDashStr.removeAt(0)
        }

        if (res.length > 0) {
            res += "-"
        }

        for (i in 0 until removeDashStr.size / k) {
            for (j in 0 until k) {
                res += removeDashStr[0].toUpperCase()
                removeDashStr.removeAt(0)
            }

            res += "-"
        }

        if (res[res.lastIndex] == '-') {
            res = res.removeRange(res.lastIndex, res.lastIndex + 1)
        }

        return res
    }
}