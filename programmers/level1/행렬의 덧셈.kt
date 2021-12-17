class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = arrayOf<IntArray>()
        
        answer = arr1.mapIndexed {
            i, arr -> arr.mapIndexed {
                j, v2 -> v2 + arr2[i][j]
            }.toIntArray()
        }.toTypedArray()
        
        return answer
    }
}