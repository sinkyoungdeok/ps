#include <iostream>
#include <vector>
#include <cmath>

#define ll long long
#define vi vector<int>
#define vll vector<ll>

#define MAX_SIZE (int)1e5

using namespace std;

int arr[MAX_SIZE];


void update_lazy(vi &tree, vi &lazy, int node, int start, int end) {
	if (lazy[node] ) {
		tree[node] =  (end - start + 1) - tree[node];

		if (start != end) { //leaf노드가 아닐 때만 전파
			lazy[node * 2] = !lazy[node*2+1];
			lazy[node * 2 + 1] = !lazy[node*2+1];
		}
		lazy[node] = 0;
	}
}

int update_range(vi &tree, vi &lazy, int node, int start, int end, int left, int right) {
	update_lazy(tree, lazy, node, start, end);

	if (right < start || end < left) return tree[node];
	else if (left <= start && end <= right) {
		tree[node] = (end - start + 1) - tree[node];

		if (start != end) {
			lazy[node * 2] = !lazy[node * 2];
			lazy[node * 2 + 1] = !lazy[node * 2 + 1];
		}

		return tree[node];
	}

	int mid = (start + end) / 2;
	return tree[node] = update_range(tree, lazy, node * 2, start, mid, left, right) + update_range(tree, lazy, node * 2 + 1, mid + 1, end, left, right);
}

int sum(vi &tree, vi &lazy, int node, int start, int end, int left, int right) {
	update_lazy(tree, lazy, node, start, end);

	if (right < start || end < left) return 0;
	else if (left <= start && end <= right) return tree[node];

	int mid = (start + end) / 2;
	return sum(tree, lazy, node * 2, start, mid, left, right) + sum(tree, lazy, node * 2 + 1, mid + 1, end, left, right);
}

int main() {
	ios::sync_with_stdio(false); cin.tie(0);
	int n, m;
	cin >> n >> m;

	int height = (int)ceil(log2(n))+1;
	vi tree(1 << height );
	vi lazy(1 << height );


	for (int i = 0; i < m ; i++) {
		int cmd, a, b;
		cin >> cmd >> a >> b;

		if (cmd == 1) {
			cout << sum(tree, lazy, 1, 1, n, a, b) << '\n';
		}
		else {
			update_range(tree, lazy, 1, 1, n, a, b);
		}
	}

	return 0;
}
