class Solution {
    fun solution(x: Int): Boolean {
        var answer = x % x.toString().toList().map{
            Character.getNumericValue(it)
        }.sum() == 0 
        
        return answer
    }
}