class Solution {
    fun solution(s: String): String {
        return s.slice( (s.length-1)/2 .. s.length/2 )
    }
}