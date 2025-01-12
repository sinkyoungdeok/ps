class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        val res = mutableListOf<Int>()
        val map = mutableMapOf<Int, Int>()
        for (i in 0 until nums2.size) {
            map[nums2[i]] = i
        }

        for (i in 0 until nums1.size) {
            val nums2i = map[nums1[i]]
            var isFind = false

            for (j in nums2i!! + 1 until nums2.size) {
                if (nums1[i] < nums2[j]) {
                    isFind = true
                    res.add(nums2[j])
                    break
                }
            }

            if (isFind == false) {
                res.add(-1)
            }
        }

        return res.toIntArray()
    }
}