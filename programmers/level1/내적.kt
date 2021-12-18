class Solution {
    fun solution(a: IntArray, b: IntArray): Int {
        return a.mapIndexed{
            i,v ->
                v * b[i]
        }.sum()
    }
}