class Solution {
    fun solution(x: Int, n: Int): LongArray {        
        return LongArray(n).mapIndexed{
            i,v -> (i+1).toLong() * x
        }.toLongArray()
    }
}