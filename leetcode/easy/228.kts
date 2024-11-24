class Solution {
    fun summaryRanges(nums: IntArray): List<String> {
        if (nums.size == 0) return listOf<String>()

        val answer = mutableListOf<String>()
        var prev = nums[0]
        var curr = nums[0]

        for (i in 1 until nums.size) {
            if ((curr + 1) != nums[i]) {
                if (prev == curr) {
                    answer.add(prev.toString())
                } else {
                    answer.add(prev.toString() + "->" + curr.toString())
                }

                prev = nums[i]
                curr = nums[i]

                continue
            }

            if ((curr + 1) == nums[i]) {
                curr = nums[i]
            }
        }

        if (prev == curr) {
            answer.add(prev.toString())
        } else {
            answer.add(prev.toString() + "->" + curr.toString())
        }

        return answer
    }
}