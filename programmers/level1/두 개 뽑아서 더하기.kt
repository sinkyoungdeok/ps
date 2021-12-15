class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer = arrayListOf<Int>() 
        
        for ((i,v) in numbers.withIndex()) {
            for (j in i+1..numbers.size-1) {
                answer.add(v + numbers[j])
            }
        }
        
        return answer.toSet().toIntArray().sortedArray()
    }
}