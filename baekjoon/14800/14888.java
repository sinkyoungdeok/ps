/* package whatever; // don't place package name! */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

/* Name of the class has to be "Main" only if the class is public. */
public class Main {

  static class Struct {

    int sum;
    int index;
    int[] oper;

    public Struct(int sum, int index, int[] oper) {
      this.sum = sum;
      this.index = index;
      this.oper = oper;
    }
  }

  static Scanner s = new Scanner(System.in);
  static int N;
  static int[] A;
  static int[] O;
  static Stack<Struct> st = new Stack<>();
  static int res_min = 1000000000;
  static int res_max = -1000000000;


  public static void main(String[] args) throws java.lang.Exception {
    // init
    N = s.nextInt();
    A = new int[N];
    O = new int[4];

    for (int i = 0; i < N; i++) {
      A[i] = s.nextInt();
    }
    for (int i = 0; i < 4; i++) {
      O[i] = s.nextInt();
    }

    Struct start = new Struct(A[0], 1, O);
    st.add(start);

    // start
    while (!st.isEmpty()) {
      Struct curr = st.pop();

      if (curr.index == N) {
        res_max = Math.max(res_max, curr.sum);
        res_min = Math.min(res_min, curr.sum);
        continue;
      }

      int next_num = A[curr.index];
      int next_index = curr.index + 1;

      for (int i = 0; i < 4; i++) {
        if (curr.oper[i] == 0) {
          continue;
        }

        switch (i) {
          case 0:
            st.add(new Struct(curr.sum + next_num, next_index,
                new int[]{curr.oper[0] - 1, curr.oper[1], curr.oper[2], curr.oper[3]}));
            break;
          case 1:
            st.add(new Struct(curr.sum - next_num, next_index,
                new int[]{curr.oper[0], curr.oper[1] - 1, curr.oper[2], curr.oper[3]}));
            break;
          case 2:
            st.add(new Struct(curr.sum * next_num, next_index,
                new int[]{curr.oper[0], curr.oper[1], curr.oper[2] - 1, curr.oper[3]}));
            break;
          case 3:
            st.add(new Struct(curr.sum / next_num, next_index,
                new int[]{curr.oper[0], curr.oper[1], curr.oper[2], curr.oper[3] - 1}));
            break;
        }
      }
    }

    System.out.println(res_max);
    System.out.println(res_min);

  }

}
