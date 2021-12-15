class Solution {
    fun solution(n: Long): Long {
        var answer = n.toString().toList().sorted().reversed().joinToString("").toLong()
        
        return answer
    }
}