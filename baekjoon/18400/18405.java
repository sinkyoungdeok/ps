/* package whatever; // don't place package name! */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/* Name of the class has to be "Main" only if the class is public. */
public class Main {

  static class Pair {

    public int i;
    public int j;

    @Override
    public String toString() {
      return "Pair{" +
          "i=" + i +
          ", j=" + j +
          '}';
    }

    public Pair(int i, int j) {
      this.i = i;
      this.j = j;
    }
  }

  static Scanner s = new Scanner(System.in);
  static int N, K;
  static int[][] board;
  static List<List<Pair>> dic = new ArrayList<>();
  static int S, X, Y;
  static int[] di = {0, 0, 1, -1};
  static int[] dj = {1, -1, 0, 0};

  public static void main(String[] args) throws java.lang.Exception {
    // init
    N = s.nextInt();
    K = s.nextInt();
    board = new int[N][N];
    for (int i = 0; i <= K; i++) {
      dic.add(new ArrayList<>());
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        board[i][j] = s.nextInt();
        if (board[i][j] == 0) {
          continue;
        }
        dic.get(board[i][j]).add(new Pair(i, j));
      }
    }
    S = s.nextInt();
    X = s.nextInt();
    Y = s.nextInt();

    // solve
    for (int s = 0; s < S; s++) {
      for (int k = 1; k <= K; k++) {
        List<Pair> newDic = new ArrayList<>();

        for (Pair curr : dic.get(k)) {
          for (int d = 0; d < 4; d++) {
            int ni = curr.i + di[d];
            int nj = curr.j + dj[d];

            if (!((0 <= ni && ni < N) && (0 <= nj && nj < N))) {
              continue;
            }
            if (board[ni][nj] != 0) {
              continue;
            }
            board[ni][nj] = k;
            newDic.add(new Pair(ni, nj));

            if (ni == X - 1 && nj == Y - 1) {
              System.out.println(board[ni][nj]);
              return;
            }
          }
        }

        dic.get(k).clear();
        dic.get(k).addAll(newDic);
      }
    }
    System.out.println(board[X - 1][Y - 1]);
  }

}
