class Solution {
  public int missingNumber(int[] nums) {
    int res = 0;

    Arrays.sort(nums);

    for (int num: nums) {
      if (res != num) {
        break;
      }

      res ++;
    }

    return res;
  }
}