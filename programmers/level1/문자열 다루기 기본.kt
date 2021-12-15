class Solution {
    fun solution(s: String): Boolean {
        if ( 4!=s.length && s.length != 6) return false 
        
        for (each in s) if (each <'0' || each > '9') return false
        return true
    }
}