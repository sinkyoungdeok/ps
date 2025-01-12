class Solution {
    fun findRelativeRanks(score: IntArray): Array<String> {
        val sortedScore = score.sorted().reversed()
        val map = mutableMapOf<Int, String>()

        for (i in 0 until sortedScore.size) {
            if (i == 0) {
                map[sortedScore[i]] = "Gold Medal"
            } else if (i == 1) {
                map[sortedScore[i]] = "Silver Medal"
            } else if (i == 2) {
                map[sortedScore[i]] = "Bronze Medal"
            } else {
                map[sortedScore[i]] = (i + 1).toString()
            }
        }

        var res = mutableListOf<String>()

        for (s in score) {
            res.add(map[s]!!)
        }

        return res.toTypedArray()
    }
}