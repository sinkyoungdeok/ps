class Solution {
    fun firstUniqChar(s: String): Int {
        val countMap = mutableMapOf<Char, Int>()
        val indexMap = mutableMapOf<Char, Int>()
        val set = mutableSetOf<Char>()

        for (i in 0 until s.length) {
            set.add(s[i])
            if (countMap.get(s[i]) == null) {
                countMap[s[i]] = 1
                indexMap[s[i]] = i
            } else {
                countMap[s[i]] = countMap[s[i]]!! + 1
            }
        }

        var res = 10000000

        for (i in set) {
            if (countMap[i]!! == 1 && res > indexMap[i]!!) {
                res = indexMap[i]!!
            }
        }

        if (res == 10000000) {
            return -1
        }

        return res
    }
}