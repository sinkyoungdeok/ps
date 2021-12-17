class Solution {
    fun solution(numbers: IntArray): Int {
        var check = IntArray(10)
        numbers.forEach {
            check[it] = 1
        }
        var answer: Int = 0
        
        for(i in 1..9) {
            if(check[i] == 0) answer+= i
        }
        
        return answer
    }
}