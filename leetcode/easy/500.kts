class Solution {
    fun findWords(words: Array<String>): Array<String> {
        val firstSet = mutableSetOf('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')
        val secondSet = mutableSetOf('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')
        val thirdSet = mutableSetOf('z', 'x', 'c', 'v', 'b', 'n', 'm')
        val res = mutableListOf<String>()

        for (w in words) {
            var f = 0
            var s = 0
            var t = 0
            for (i in w) {
                if (firstSet.contains(i.toLowerCase())) {
                    f = 1
                }

                if (secondSet.contains(i.toLowerCase())) {
                    s = 1
                }

                if (thirdSet.contains(i.toLowerCase())) {
                    t = 1
                }
            }

            if (f + s + t == 1) {
                res.add(w)
            }
        }

        return res.toTypedArray()
    }
}