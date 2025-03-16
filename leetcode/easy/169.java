class Solution {
  public int majorityElement(int[] nums) {
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    for (int num: nums) {
      map.put(num, map.getOrDefault(num, 0) + 1);
    }

    int res = 0;
    int maxCnt = 0;

    for (int key: map.keySet()) {
      int value = map.get(key);

      if (maxCnt < value) {
        res = key;
        maxCnt = value;
      }
    }

    return res;
  }
}