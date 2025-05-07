import java.io.*;
import java.util.*;

public class Main {

  static int[][] map;
  static int n;
  static int m;
  static boolean[][] visited;
  static int[] dx = { -1, 1, 0, 0 };
  static int[] dy = { 0, 0, -1, 1 };

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    m = Integer.parseInt(st.nextToken());

    map = new int[n][m];
    for (int i = 0; i < n; i++) {
      String s = br.readLine();
      for (int j = 0; j < m; j++) {
        map[i][j] = s.charAt(j) - '0';
      }
    }

    visited = new boolean[n][m];
    visited[0][0] = true;

    int startX = 0;
    int startY = 0;

    Queue<int []> q = new LinkedList<>();
    q.add(new int[] { startX, startY });

    while(!q.isEmpty()) {
      int now[] = q.poll();
      int currX = now[0];
      int currY = now[1];

      for (int i = 0; i < 4; i++) {
        int nextX = currX + dx[i];
        int nextY = currY + dy[i];

        if (nextX < 0 || nextY < 0 || nextX >= n || nextY >= m) continue;
        if (map[nextX][nextY] == 0) continue;
        if (visited[nextX][nextY]) continue;

        q.add(new int[] { nextX, nextY });
        map[nextX][nextY] = map[currX][currY] + 1;
        visited[nextX][nextY] = true;
      }
    }

    System.out.println(map[n - 1][m - 1]);
  }
}