class Solution {
    fun generate(numRows: Int): List<List<Int>> {
        val answer: MutableList<List<Int>> = mutableListOf()

        answer.add(listOf(1))

        for (i in 0 until numRows - 1) {
            val temp = mutableListOf(1)
            for (j in 0 until answer[i].size - 1) {
                temp.add(answer[i][j] + answer[i][j+1])
            }

            temp.add(1)

            answer.add(temp)
        }

        return answer
    }
}