class Solution {
  public int removeDuplicates(int[] nums) {
    int res = 0;

    if (nums.length >= 1) res ++;

    for (int i = 1; i < nums.length; i++) {
      if(nums[i] == nums[i-1]) continue;
      nums[res] = nums[i];
      res++;
    }

    return res;
  }
}