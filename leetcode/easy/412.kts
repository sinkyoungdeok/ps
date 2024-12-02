class Solution {
    fun fizzBuzz(n: Int): List<String> {
        val res = mutableListOf<String>()

        for (i in 1 until n + 1) {
            if (i % 15 == 0) res.add("FizzBuzz")
            else if (i % 3 ==0) res.add("Fizz")
            else if (i % 5 ==0) res.add("Buzz")
            else res.add(i.toString())
        }

        return res
    }
}