#include <iostream>
#include <queue>
#include <vector>
#include <functional>
using namespace std;
int main()
{
	int N, K;
	cin >> N >> K;
	bool visit[100501] = { 0 };
	priority_queue<pair<int, int>,vector<pair<int,int>>, greater<pair<int,int>>> pq;

	pq.push(pair<int, int>(0, N));
	visit[N] = true;
	while (!pq.empty())
	{
		int second = pq.top().first;
		int position = pq.top().second;
		pq.pop();
		if (position == K)
		{
			cout << second << endl;
			return 0;
		}

		second++;
		if (position - 1 >= 0 && !visit[position - 1])
		{
			pq.push(pair<int, int>(second, position - 1));
			visit[position - 1] = true;
		}
		if (position + 1 <= 100500 && !visit[position + 1])
		{
			pq.push(pair<int, int>(second, position + 1));
			visit[position + 1] = true;
		}
		if (position * 2 <= 100500 && !visit[position * 2])
		{
			pq.push(pair<int, int>(second, position * 2));
			visit[position * 2] = true;
		}


	}


	return 0;
}