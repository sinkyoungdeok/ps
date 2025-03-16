class Solution {
  public int maxProfit(int[] prices) {
    int min = 1000000000;
    int res = 0;

    for (int p : prices) {
      if (min != 1000000000 && p - min > 0) {
        res = Math.max(res, p - min);
      }

      min = Math.min(min, p);
    }

    return res;
  }
}