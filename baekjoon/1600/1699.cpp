#include <iostream>
#include <algorithm>
using namespace std;

int dp[100001];

int main() 
{
	int N;
	cin >> N;

	for (int i = 0; i <= N; i++)
	{
		dp[i] = i;
	}

	for (int i = 2; i <= N; i++)
	{
		for (int j = 2; j*j <= i; j++)
		{
			dp[i] = min(dp[i], dp[i - j * j] + 1);
		}
	}

	cout << dp[N] << '\n';


	return 0;
}

