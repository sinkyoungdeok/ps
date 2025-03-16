class Solution {
  public int[] plusOne(int[] digits) {
    int leng = digits.length;
    digits[leng-1] += 1;
    int carry = 0;

    for (int i = leng-1; i >=0; i--) {
      digits[i] += carry;
      carry = 0;

      if (digits[i] == 10) {
        digits[i] = 0;
        carry = 1;
      }
    }

    if (carry == 1) {
      int[] newArray = new int[leng + 1];

      newArray[0] = carry;
      for (int i = 1; i< leng + 1; i++) {
        newArray[i] = digits[i-1];
      }

      return newArray;
    }
    return digits;
  }
}