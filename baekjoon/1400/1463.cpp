#include <iostream>
#include <queue>
#include <functional>
using namespace std;
int main()
{
	//priority_queue<int,vector<int>,greater<int>> pq;
	
	queue<int> q;
	queue<int> q2;

	int N;
	cin >> N;
	
	q.push(N);
	int n = 0;
	if (N == 1)
	{
		cout << 0 << endl;
		return 0;
	}
	while (1)
	{
		while (!q.empty())
		{
			int cur = q.front(); q.pop();
			q2.push(cur);

			if (cur == 1)
			{
				cout << n << endl;
				return 0;
			}

		}
		while (!q2.empty())
		{
			int cu = q2.front(); q2.pop();
			if (cu % 3 == 0)
				q.push(cu / 3);
			if (cu % 2 == 0)
				q.push(cu / 2);
			q.push(cu - 1);
		}
		n++;
	}



	return 0;
}