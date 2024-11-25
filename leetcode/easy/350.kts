class Solution {
    fun intersect(nums1: IntArray, nums2: IntArray): IntArray {
        nums1.sort()
        nums2.sort()
        val res = mutableListOf<Int>()
        var i = 0
        var j = 0
        while(nums1.size > i && nums2.size > j) {
            if (nums1[i] < nums2[j]) {
                i ++
                continue
            }

            if (nums1[i] > nums2[j]) {
                j ++
                continue
            }

            res.add(nums1[i])
            i++
            j++
        }

        return res.toIntArray()
    }
}