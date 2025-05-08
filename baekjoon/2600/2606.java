import java.io.*;
import java.util.*;

public class Main {
  static int N, M;
  static int[][] adj;
  static int[] check;
  static int count = 0;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    M = Integer.parseInt(br.readLine());

    adj = new int[N+1][N+1];
    check = new int[N+1];

    for (int i = 0; i< M; i++) {
      StringTokenizer str = new StringTokenizer(br.readLine());

      int a = Integer.parseInt(str.nextToken());
      int b = Integer.parseInt(str.nextToken());

      adj[a][b] = adj[b][a] = 1;
    }

    dfs(1);
    System.out.println(count - 1);
  }

  public static void dfs(int curr) {
    check[curr] = 1;
    count ++;

    for (int i = 1; i <= N; i++) {
      if (check[i] == 1) continue;

      if (adj[curr][i] == 0) continue;

      dfs(i);
    }
  }
}