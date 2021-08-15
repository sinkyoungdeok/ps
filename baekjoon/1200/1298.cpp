#include <iostream>
#include <vector>
using namespace std;

int N, M, ans = 0;
int B[5005]; // A =  소 , B = 축사
vector<int> v[5005];
bool visited[5005];

bool dfs(int start)
{
	visited[start] = 1;

	for (int &i : v[start])
	{
		if (B[i] == -1 || (!visited[B[i]] && dfs(B[i])))
		{
			B[i] = start;

			return true;
		}

	}
	return false;
}

int main()
{
	cin >> N >> M;

	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
	}
	fill(B, B + N+5, -1);

	for (int i = 1; i <= N; i++)
	{
			fill(visited, visited + N+5, false);
			if (dfs(i)) ans++;
	}
	cout << ans << '\n';

}