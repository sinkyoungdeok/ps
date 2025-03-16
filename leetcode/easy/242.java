class Solution {
  public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;
    String[] ss = s.split("");
    String[] tt = t.split("");

    Arrays.sort(ss);
    Arrays.sort(tt);

    for (int i = 0; i< ss.length; i++) {

      if (!ss[i].equals(tt[i])) {
        return false;
      }
    }

    return true;
  }
}