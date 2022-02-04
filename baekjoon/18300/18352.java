/* package whatever; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner s = new Scanner(System.in);

    int N = s.nextInt();
    int M = s.nextInt();
    int K = s.nextInt();
    int X = s.nextInt() - 1;

    List<List<Integer>> adj = new ArrayList<>();
    int[] visited = new int[300001];

    for (int i = 0; i < N; i++) {
      adj.add(new ArrayList<>());
      visited[i] = -1;
    }
    visited[X] = 0;

    for (int i = 0; i < M; i++) {
      int A = s.nextInt() - 1;
      int B = s.nextInt() - 1;

      adj.get(A).add(B);
    }

    Queue<Integer> q = new LinkedList<>();
    q.add(X);

    while (!q.isEmpty()) {
      int curr = q.poll();

      adj.get(curr).stream().filter(next -> visited[next] == -1)
          .forEach(next -> {
            visited[next] = visited[curr] + 1;
            q.add(next);
          });
    }
    
    boolean check = true;
    for (int i = 0; i < N; i++) {
      if (visited[i] == K) {
        System.out.println(i+1);
        check = false;
      }
    }

    if (check) {
      System.out.println(-1);
    }
	}
}