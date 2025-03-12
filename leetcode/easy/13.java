class Solution {
  public int romanToInt(String s) {
    HashMap<String, Integer> map = new HashMap<String, Integer>();
    map.put("I", 1);
    map.put("V", 5);
    map.put("X", 10);
    map.put("L", 50);
    map.put("C", 100);
    map.put("D", 500);
    map.put("M", 1000);

    long sum = 0;

    for (int i=0; i< s.length(); i++) {
      sum += map.get(s.charAt(i) + "");

      if (i == 0) continue;

      int prev = map.get(s.charAt(i - 1) + "");
      int curr = map.get(s.charAt(i) + "");
      if (prev < curr) {
        sum -= 2 * prev;
      }
    }

    return sum;
  }
}