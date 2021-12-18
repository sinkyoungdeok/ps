class Solution {
    fun solution(s: String): String {
        return s.split(" ").joinToString(" ") { it ->
            it.mapIndexed{ i, v -> 
                if(i % 2 == 0) v.toUpperCase() 
                else v.toLowerCase()
            }.joinToString("")
        }
    }
}