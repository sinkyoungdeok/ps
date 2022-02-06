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
    static int N;
    static char[][] board;
    static List<Pair> T = new ArrayList<>();
    static List<Pair> O = new ArrayList<>();
    static List<Pair> o = new ArrayList<>();
    static int[] di = {0, 0, 1, -1};
    static int[] dj = {1, -1, 0, 0};
    static Boolean check = true;


    public static void main(String[] args) throws java.lang.Exception {
        N = s.nextInt();
        board = new char[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                board[i][j] = s.next().charAt(0);
                if (board[i][j] == 'X') {
                    O.add(new Pair(i, j));
                } else if (board[i][j] == 'T') {
                    T.add(new Pair(i, j));
                }
            }
        }

        combination(-1, 0);

        if(check) {
            System.out.println("NO");
        }
    }

    public static void combination(int index, int size) {
        if (!check) {
            return;
        }

        if (size == 3) {
            o.forEach(c -> board[c.i][c.j] = 'O');

            if (simulation()) {
                check = false;
                System.out.println("YES");
            }

            o.forEach(c -> board[c.i][c.j] = 'X');
            return;
        }

        for (int i = index + 1; i < O.size(); i++) {
            o.add(O.get(i));
            combination(i, size + 1);
            o.remove(o.size() - 1);
        }
    }

    public static boolean simulation() {
        for (int i = 0; i < T.size(); i++) {
            for (int d = 0; d < 4; d++) {
                if (search(T.get(i).i, T.get(i).j, d)) {
                    return false;
                }
            }
        }

        return true;
    }

    public static boolean search(int ci, int cj, int d) {
        if (board[ci][cj] == 'S') {
            return true;
        }
        if (board[ci][cj] == 'O') {
            return false;
        }
        int ni = ci + di[d];
        int nj = cj + dj[d];
        if (!(0 <= ni && ni < N && 0 <= nj && nj < N)) {
            return false;
        }

        return search(ni, nj, d);
    }
}
