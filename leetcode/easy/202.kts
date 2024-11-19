import java.util.*

class Solution {
    fun isHappy(n: Int): Boolean {
        val hashMap = HashSet<Int>()
        var temp = n

        while (true) {
            var sum = 0

            while (temp > 0) {
                val t = temp % 10
                sum += t * t
                temp /= 10
            }

            if (sum == 1) {
                return true
            }

            if (!hashMap.contains(sum)) {
                hashMap.add(sum)
            } else {
                return false
            }

            temp = sum
        }

        return false
    }
}