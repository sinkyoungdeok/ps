class Solution {
    fun solution(phone_number: String): String {
        var answer = ""
        
        answer = phone_number.toList().mapIndexed{
            i, v -> 
                if(i < phone_number.length - 4) "*"
                else v
        }.joinToString("")

        
        return answer
    }
}