#include <iostream>
using namespace std;
int main()
{
	int N,M;
	cin >> N >> M;
	
	int **dist = new int*[N];
	for (int i = 0; i < N; i++)
	{
		dist[i] = new int[N];
		for (int j = 0; j < N; j++)
		{
			if (i == j)
				dist[i][j] = 0;
			else
				dist[i][j] = 10000000;
		}
	}

	for (int i = 0; i < M; i++)
	{
		int A, B;
		cin >> A >> B;
		
		dist[A - 1][B - 1] = 1;
		dist[B - 1][A - 1] = 1;
	}

	for(int k=0; k< N;k++)
		for(int i=0;i<N;i++)
			for (int j = 0; j < N; j++)
			{
				if (dist[i][j] > dist[i][k]+ dist[k][j])
					dist[i][j] = dist[i][k] + dist[k][j];
			}

	int min_sum = 100000000;
	int min_sum_result = 0;
	for (int i = 0; i < N; i++)
	{
		int sum = 0;
		for (int j = 0; j < N; j++)
			sum += dist[i][j];
		if (min_sum > sum)
		{
			min_sum = sum;
			min_sum_result = i + 1;
		}

	}
	cout << min_sum_result << endl;
	return 0;
}