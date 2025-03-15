class Solution {
  public int strStr(String haystack, String needle) {
    int j = 0;
    for (int i = 0; i< haystack.length(); i++) {
      if (haystack.charAt(i) == needle.charAt(j)) {
        j ++;
      } else {
        i -= j;
        j = 0;
      }

      if (needle.length() == j) {
        return i - j + 1;
      }
    }

    return -1;
  }
}