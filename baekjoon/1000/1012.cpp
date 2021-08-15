#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
#include <stack>
using namespace std;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int T;
	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
		int M, N, K;
		cin >> N >> M >> K;
		bool cabbage[51][51] = { false };
		bool visited[51][51] = { false };
		
		for (int k = 0; k < K; k++)
		{
			int X, Y;
			cin >> X >> Y;
			cabbage[X][Y] = true;
		}
		int di_x[4] = { 1,-1,0,0 };
		int di_y[4] = { 0,0,1,-1 };
		int result = 0;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				if (!visited[i][j] && cabbage[i][j])
				{
					result++;
					stack<pair<int, int>> st;
					st.push(pair<int, int>(i, j));
					while (!st.empty())
					{
						int cu_x = st.top().first;
						int cu_y = st.top().second; st.pop();

						for (int d = 0; d < 4; d++)
						{
							int ne_x = cu_x + di_x[d];
							int ne_y = cu_y + di_y[d];
							if (ne_x < 0 || ne_y < 0 || visited[ne_x][ne_y] || !cabbage[ne_x][ne_y]||ne_x >=N || ne_y>=M)
								continue;
							visited[ne_x][ne_y] = true;
							st.push(pair<int, int>(ne_x, ne_y));
						}



					}
				}
			}
		}
		cout << result << endl;

	}
	

	return 0;
}