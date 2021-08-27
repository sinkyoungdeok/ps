#include <iostream>
#include <queue>
#include <vector>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t;
	int n, k, w;
	vector<vector<int> > p;
	vector<int> dist, times, indeg;

	cin >> n;
	dist.resize(n + 1);
	times.resize(n + 1,0);
	indeg.resize(n + 1);
	p.resize(n + 1);
	for (int i = 0; i < n; i++) {
		int u;
		cin >> u;
		times[i + 1] = u;

		int v;
		cin >> v;
		while (v != -1)
		{
			p[v].push_back(i+1);
			indeg[i+1]++;
			cin >> v;
		}
	}

	queue<int> q;
	for (int i = 1; i < n + 1; i++) {
		if (indeg[i] == 0) {
			q.push(i);
			dist[i] = times[i];
		}
	}
	while (!q.empty()) {
		int now = q.front();
		q.pop();

		for (int &next : p[now]) {
			if (--indeg[next] == 0)
				q.push(next);
			if (dist[next] < dist[now] + times[next]) {
				dist[next] = dist[now] + times[next];
			}
		}
	}
	for (int i = 1; i <= n; i++)
		cout << dist[i] << endl;
}