#include <cstdio>

int main() {
    int e, s, m;
    scanf("%d %d %d", &e, &s, &m);
    int year = 0;
    while (true) {
        int x = year%15, y = year%28, z = year%19;
        if (x == e-1 && y == s-1 && z == m-1) break;
        year++;
    }
    printf("%d\n", year+1);
    return 0;
}