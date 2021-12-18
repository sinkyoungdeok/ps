class Solution {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer: Int = 0
        
        for(i in 0..absolutes.size-1) {
            if(signs[i]) {
                answer += absolutes[i]
            } else {
                answer -= absolutes[i]
            }
        }
        
        return answer
    }
}