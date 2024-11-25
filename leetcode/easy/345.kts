class Solution {
    fun reverseVowels(s: String): String {
        var start = 0
        var end = s.lastIndex
        val set = setOf<Char>('a','e','i','o','u','A','E','I','O','U')
        var res = s.toCharArray()

        while (start < end) {
            if (res[start] !in set) start++
            if (res[end] !in set) end--

            if (res[start] in set && res[end] in set) {
                val temp = res[start]
                res[start] = res[end]
                res[end] = temp

                start++
                end--
            }
        }

        return String(res)
    }
}