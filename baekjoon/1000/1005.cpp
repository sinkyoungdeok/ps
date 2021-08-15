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
	cin >> t;
	while (t--) {
		dist.clear();
		times.clear();
		indeg.clear();
		p.clear();
		
		cin >> n >> k;
		dist.resize(n + 1);
		times.resize(n + 1);
		indeg.resize(n + 1);
		p.resize(n + 1);
		for (int i = 1; i < n + 1; i++) {
			cin >> times[i];
		}
		for (int i = 0; i < k; i++) {
			int u, v;
			cin >> u >> v;
			p[u].push_back(v);
			indeg[v]++;
		}
		cin >> w;
		
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
			if (now == w) break;
			
			for (int &next : p[now]) {
				if (--indeg[next]== 0)
					q.push(next);
				if (dist[next] < dist[now] + times[next]) {
					dist[next] = dist[now] + times[next];
				}
			}
		}
		cout << dist[w] << '\n';
	}
}