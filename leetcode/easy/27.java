class Solution {
  public int removeElement(int[] nums, int val) {
    int res = 0;

    for(int i = 0; i< nums.length; i++) {
      if (nums[i] == val) continue;
      nums[res++] = nums[i];
    }

    return res;
  }
}