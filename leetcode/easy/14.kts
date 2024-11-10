class Solution {
    fun longestCommonPrefix(strs: Array<String>): String {
        var res = StringBuilder()
        val firstStr = strs[0]

        for (i in 0 until firstStr.length) {
            for (str in strs) {
                if (str.length <= i || str[i] != firstStr[i]) {
                    return res.toString()
                }
            }
            res.append(firstStr[i])
        }

        return res.toString()
    }
}