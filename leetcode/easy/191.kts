class Solution {
    fun hammingWeight(n: Int): Int {
        var t = n
        var res = ""

        while(t > 0) {
            res += t % 2
            t /= 2
        }

        return res.count { it == '1' }
    }
}