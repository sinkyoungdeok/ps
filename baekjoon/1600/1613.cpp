#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;
int main()
{
	int n, k;
	
	scanf("%d %d", &n, &k);

	int **dist = new int*[n];
	for (int i = 0; i < n; i++)
	{
		dist[i] = new int[n];
		for (int j = 0; j < n; j++)
		{
			if (i == j)
				dist[i][j] = 0;
			else
				dist[i][j]= 1000000000;
		}
	}
	for (int i = 0; i < k; i++)
	{
		int k1, k2;
		scanf("%d %d", &k1, &k2);

		dist[k1-1][k2-1] = 1;
	}

	for (int K = 0; K < n; K++)
	{
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if ((dist[i][K] + dist[K][j]) == 2)
				{
					dist[i][j] = 1;
				}
			}
		}
	}
	int s;
	scanf("%d", &s);
	for (int i = 0; i < s; i++)
	{
		int s1, s2;
		scanf("%d %d", &s1, &s2);
		if (dist[s1 - 1][s2 - 1] == 1)
			printf("-1\n");
		else if (dist[s2 - 1][s1 - 1] == 1)
			printf("1\n");
		else
			printf("0\n");
	}

	return 0;
}