#include <iostream>
using namespace std;
int main() 
{
	int n = 0;
	cin >> n;
	int **num = new int*[n + 1];
	for (int i = 1; i <= n; i++)
	{
		num[i] = new int[5];
		for (int j = 0; j < 5; j++)
			cin >> num[i][j];
	}
	int *check = new int[n + 1];
	for (int i = 1; i <= n; i++)
		check[i] = 0;
	int max = 0;
	int *check_st = new int[n + 1];
	for (int i = 1; i <= n; i++)
	{
		for (int q = 1; q <= n; q++)
			check_st[q] = 0;
		for (int j = 0; j < 5; j++)
		{
			for (int k = 1; k <= n; k++)
			{
				if (num[k][j] == num[i][j])
					check_st[k] = 1;

			}

		}
		for (int j = 1; j <= n; j++)
		{
			if (check_st[j] == 1)
				check[i]++;
		}
		if (max < check[i])
			max = check[i];

	}

	for (int i = 1; i <= n; i++)
	{
		if (max == check[i])
		{
			cout << i << endl;
			return 0;
		}
	}

	return 0;
}