class Solution {
    fun solution(a: Int, b: Int): Long {
        var answer: Long = 0
        
        var num1 = a
        var num2 = b
        
        if (a > b) {
            num1 = b
            num2 = a
        } 
        
        for(i: Int in num1..num2) answer += i
        
        return answer
    }
}