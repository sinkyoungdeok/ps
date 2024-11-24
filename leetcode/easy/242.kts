class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        return s.split("").sorted() == t.split("").sorted()
    }
}