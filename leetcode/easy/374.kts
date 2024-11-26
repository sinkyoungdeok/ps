/**
 * The API guess is defined in the parent class.
 * @param  num   your guess
 * @return         -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * fun guess(num:Int):Int {}
 */

class Solution : GuessGame() {
    override fun guessNumber(n: Int): Int {
        var right = n.toLong()
        var left = 1L
        var mid = -1L

        while (true) {
            mid = (left + right) / 2L

            val res = guess(mid.toInt())

            if (res == 0) return mid.toInt()

            if (res == -1) right = mid
            else left = mid + 1
        }

        return -1
    }
}