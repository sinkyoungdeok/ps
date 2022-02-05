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

  static int board[][];
  static int map[][];
  static int N;
  static int M;
  static List<Pair> wall;
  static List<Pair> combWall;
  static int ans;


  public static void main(String[] args) throws java.lang.Exception {
    Scanner s = new Scanner(System.in);

    N = s.nextInt();
    M = s.nextInt();
    board = new int[N][M];
    map = new int[N][M];
    wall = new ArrayList<>();
    combWall = new ArrayList<>();
    ans = 0;

    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        board[i][j] = s.nextInt();
        if (board[i][j] == 0) {
          wall.add(new Pair(i, j));
        }
      }
    }

    solve(-1, 0);
    System.out.println(ans);
  }

  public static void solve(int index, int size) {
    if (size == 3) {
      for (int i = 0; i < N; i++) for (int j = 0; j < M; j++) map[i][j] = board[i][j];
      combWall.forEach(w -> map[w.i][w.j] = 1);
      diffusion();
      ans = Math.max(ans, count());
      return;
    }

    for (int i = index + 1; i < wall.size(); i++) {
      combWall.add(wall.get(i));
      solve(i, size + 1);
      combWall.remove(combWall.size() - 1);
    }
  }

  public static void diffusion() {
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if(map[i][j] == 2) {
          dfs(i,j);
        }
      }
    }
  }

  public static void dfs(int ci, int cj) {
    int[] di = {0, 0, 1, -1};
    int[] dj = {1, -1, 0, 0};

    for (int d = 0; d < 4; d++) {
      int ni = ci + di[d];
      int nj = cj + dj[d];

      if (!((0 <= ni && ni < N) && (0 <= nj && nj < M))) continue;
      if (map[ni][nj] != 0) continue;
      map[ni][nj] = -1;
      dfs(ni,nj);
    }
  }

  public static int count() {
    int count = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < M; j++) {
        if(map[i][j] == 0) count += 1;
      }
    }
    return count;
  }

}
