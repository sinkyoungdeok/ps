class Solution {
  public boolean isPalindrome(int x) {
    String s = x + "";

    for (int i = 0; i< s.length()/2; i++) {
      if (s.chatAt(i) != s.charAt(s.length() - i - 1)) {
        return false;
      }
    }

    return true;
  }
}