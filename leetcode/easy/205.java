class Solution {
  public boolean isIsomorphic(String s, String t) {
    HashMap<Character, Character> sMap = new HashMap<Character, Character>();
    HashMap<Character, Character> tMap = new HashMap<Character, Character>();

    for (int i = 0; i< s.length(); i++) {
      char sc = s.charAt(i);
      char tc = t.charAt(i);

      Character findC = sMap.get(sc);
      Character findT = tMap.get(tc);

      if (findC == null && findT == null) {
        sMap.put(sc, tc);
        tMap.put(tc, sc);
      } else if(findC != null && findT != null) {
        if (findC != tc) {
          return false;
        }
      } else {
        return false;
      }

    }

    return true;
  }
}