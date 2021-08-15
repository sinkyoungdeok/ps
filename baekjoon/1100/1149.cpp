#include <iostream>
using namespace std;
int house[1001][3];
int visit[1001][3];
int main()
{
	int N;
	cin >> N;
	
	for (int i = 0; i < N; i++)
		for (int j = 0; j < 3; j++)
		{
			cin >> house[i][j];
			visit[i][j] = 1000000000;
		}
	visit[0][0] = house[0][0];
	visit[0][1] = house[0][1];
	visit[0][2] = house[0][2];

	for (int i = 1; i < N; i++)
	{
		for (int j = 0; j < 3; j++)
		{
			for (int k = 0; k < 3; k++)
			{
				if (j == k)
					continue;

				if ((visit[i - 1][j] + house[i][k]) < visit[i][k])
					visit[i][k] = visit[i - 1][j] + house[i][k];
			}
		}

	}

	int min = 10000000000;
	for (int i = 0; i < 3; i++)
		if (min > visit[N - 1][i])
			min = visit[N - 1][i];
	cout << min << endl;

	return 0;
}