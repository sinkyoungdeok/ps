class Solution {
    fun solution(n: Long): IntArray {
        return n.toString().reversed().map{
            it.toInt() - '0'.toInt()
        }.toIntArray()
    }
}