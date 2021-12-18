class Solution {
    fun solution(num2: Int): Int {
        var num = num2
        
        if(num == 1) return 0
        
        for (i in 1..500) {
            if(num % 2 ==0) num = num/2
            else if(num % 2 == 1) num = num*3 + 1
            
            if(num == 1) return i
        }
        
        return -1
    }
}