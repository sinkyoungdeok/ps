class Solution {
  public int lengthOfLastWord(String s) {
    String[] strs = s.strip().split(" ");

    return strs[strs.length - 1].length();
  }
}