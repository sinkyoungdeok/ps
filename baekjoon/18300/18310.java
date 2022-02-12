/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;
import java.util.stream.Collectors;

/* Name of the class has to be "Main" only if the class is public. */
public class Main {

  private static Scanner s = new Scanner(System.in);

  public static void main(String[] args) throws java.lang.Exception {
    int N = s.nextInt();
    List<Integer> nums = new ArrayList<>();

    for (int i = 0; i < N; i++) {
      nums.add(s.nextInt());
    }

    nums = nums.stream()
        .sorted()
        .collect(Collectors.toList());

    System.out.println(nums.get((N-1)/2));
  }
}