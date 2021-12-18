class Solution {
    fun solution(n: Long): Long {
        for (i in 1 .. 100000000) {
            if(i*i.toLong() == n) return (i+1) * (i+1).toLong()
        }
        
        return -1
    }
}