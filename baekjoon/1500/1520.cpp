#include <iostream>
#include <cstring>
using namespace std;

int N, M;
int map[501][501];
int dp[501][501];
int di[4] = { 0,0,-1,1 };
int dj[4] = { -1,1,0,0 };

int solve(int i, int j)
{
	if (i == N - 1 && j == M - 1) return 1;
	int &ret = dp[i][j];
	
	if (ret != -1) return ret;
	ret = 0;

	for (int d = 0; d < 4; d++)
	{
		int ni = di[d] + i;
		int nj = dj[d] + j;

		if (0 > ni || 0 > nj || ni >= N || nj >= M)
			continue;
		if (map[i][j] > map[ni][nj])
			ret += solve(ni, nj);


	}
	

	return ret;
}

int main() 
{
	cin >> N >> M;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			cin >> map[i][j];
	memset(dp, -1, sizeof(dp));
	
	cout << solve(0, 0) << '\n';
	

	return 0;
}

