/* package whatever; // don't place package name! */
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Main {

  static class KYS {

    public String name;
    public int k;
    public int y;
    public int s;

    public String getName() {
      return name;
    }

    public int getK() {
      return k;
    }

    public int getY() {
      return y;
    }

    public int getS() {
      return s;
    }

    public KYS(String name, int k, int y, int s) {
      this.name = name;
      this.k = k;
      this.y = y;
      this.s = s;
    }
  }

  private static Scanner s = new Scanner(System.in);

  public static void main(String[] args) throws java.lang.Exception {
    int N = s.nextInt();
    List<KYS> kysList = new ArrayList<>();

    for (int i = 0; i < N; i++) {
      String name = s.next();
      int K = s.nextInt();
      int Y = s.nextInt();
      int S = s.nextInt();

      kysList.add(new KYS(name, K, Y, S));
    }

    kysList.stream()
        .sorted(Comparator
            .comparing(KYS::getK).reversed()
            .thenComparing(KYS::getY)
            .thenComparing(Comparator.comparing(KYS::getS).reversed())
            .thenComparing(KYS::getName)
        )
        .map(kys -> kys.name)
        .forEach(System.out::println);
  }
}