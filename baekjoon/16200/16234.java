import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
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
  static int N, L, R;
  static int[][] board;
  static int[] di = {0, 0, 1, -1};
  static int[] dj = {1, -1, 0, 0};
  static int res = 0;
  static boolean[][] visited;

  public static void main(String[] args) throws java.lang.Exception {
    N = s.nextInt();
    L = s.nextInt();
    R = s.nextInt();
    board = new int[N][N];
    boolean check = true;
    visited = new boolean[N][N];
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        board[i][j] = s.nextInt();
      }
    }

    while (check) {
      check = false;
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          visited[i][j] = false;
        }
      }

      for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
          if (visited[i][j]) {
            continue;
          }
          visited[i][j] = true;
          List<Pair> moving = bfs(i, j);
          if (moving.size() <= 1) {
            continue;
          }

          check = true;
          int moving_res = moving.stream()
              .map(pair -> board[pair.i][pair.j])
              .mapToInt(t -> t)
              .sum() / moving.size();

          moving.forEach(p -> board[p.i][p.j] = moving_res);
        }
      }

      if(check) {
        res++;
      }
    }
    System.out.println(res);
  }

  public static List<Pair> bfs(int curr_i, int curr_j) {
    Queue<Pair> q = new LinkedList<>();
    q.add(new Pair(curr_i, curr_j));

    List<Pair> movingPeople = new ArrayList<>();
    movingPeople.add(new Pair(curr_i, curr_j));

    while (!q.isEmpty()) {
      Pair curr = q.poll();
      for (int d = 0; d < 4; d++) {
        int ni = curr.i + di[d];
        int nj = curr.j + dj[d];
        if (!(0 <= ni && ni < N && 0 <= nj && nj < N)) {
          continue;
        }
        if (visited[ni][nj]) {
          continue;
        }
        if (!(L <= Math.abs(board[ni][nj] - board[curr.i][curr.j])
            && Math.abs(board[ni][nj] - board[curr.i][curr.j]) <= R)) {
          continue;
        }
        visited[ni][nj] = true;
        q.add(new Pair(ni, nj));
        movingPeople.add(new Pair(ni, nj));
      }
    }
    return movingPeople;
  }
}