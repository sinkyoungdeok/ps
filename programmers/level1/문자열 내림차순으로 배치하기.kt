class Solution {
    fun solution(s: String): String {
        var answer = s.toList().sorted().reversed().joinToString(separator = "")
        return answer
    }
}