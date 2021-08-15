#include <cstdio>
#include <stack>
#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int N, M, V;
	cin >> N >> M >> V;

	int **dist = new int*[N];
	int *visit_list_s = new int[N];
	int *visit_list_q = new int[N];
	for (int i = 0; i < N; i++)
	{
		dist[i] = new int[N];
		visit_list_s[i] = 0;
		visit_list_q[i] = 0;
		for (int j = 0; j < N; j++)
			dist[i][j] = 0;
	}

	for (int i = 0; i < M; i++)
	{
		int a, b;
		cin >> a >> b;
		
		dist[a - 1][b - 1] = 1;
		dist[b - 1][a - 1] = 1;
	}
	
	stack<int> st;
	st.push(V - 1);
	bool end;
	while (!st.empty())
	{
		int tmp = st.top(); st.pop();
        if(visit_list_s[tmp] == 1)
            continue;
		visit_list_s[tmp] = 1;
		cout << tmp + 1 << " ";
		end = true;
		for (int i = 0; i < N; i++)
		{
			if (visit_list_s[i] == 0)
			{
				end = false;
				break;
			}
		}
		if (end)
			break;
		
		
		
		for (int i = N-1; i >=0; i--)
		{
			if ((dist[tmp][i] || dist[i][tmp]) && visit_list_s[i]==0)
				st.push(i);
		}
	}
	cout << endl;

	queue<int> q;
	q.push(V - 1);
	while (!q.empty())
	{
		int tmp = q.front(); q.pop();
        if(visit_list_q[tmp] == 1)
            continue;
		visit_list_q[tmp] = 1;
		cout << tmp + 1 << " ";
		end = true;
		for (int i = 0; i < N; i++)
		{
			if (visit_list_q[i] == 0)
			{
				end = false;
				break;
			}
		}
		if (end)
			break;
		
		
		for (int i = 0; i < N; i++)
		{
			if ((dist[tmp][i] || dist[i][tmp]) && visit_list_q[i] == 0)
				q.push(i);
		}
	}
    cout << endl;

	return 0;
}