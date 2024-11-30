class Solution {
    fun readBinaryWatch(turnedOn: Int): List<String> {
        if (turnedOn > 8) return listOf()

        val hours = listOf(1, 2, 4, 8)
        val minutes = listOf(1, 2, 4, 8 , 16, 32)
        val res = mutableListOf<String>()

        dfs(hours, minutes, 0, 0, res, 0, turnedOn, 0, 0)
        return res.toSet().toList().sorted()
    }

    fun dfs(
        hours: List<Int>,
        minutes: List<Int>,
        ch: Int,
        cm: Int,
        res: MutableList<String>,
        cnt: Int,
        turnedOn: Int,
        hi: Int,
        mi: Int,
    ) {
        if (cnt == turnedOn) {
            if (ch < 12 && cm < 60) {
                res.add("${ch}:${cm.toString().padStart(2, '0')}")
            }

            return
        }

        for (h in hi until hours.size) {
            dfs(hours, minutes, ch + hours[h], cm, res, cnt + 1, turnedOn, h + 1, mi)
        }

        for (m in mi until minutes.size) {
            dfs(hours, minutes, ch, cm + minutes[m], res, cnt + 1, turnedOn, hi, m + 1)
        }
    }
}