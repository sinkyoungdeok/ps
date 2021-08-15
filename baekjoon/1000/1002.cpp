#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cmath>
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
		int x1, x2, y1, y2, r1, r2;
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		double dis = sqrt((x2 - x1)* (x2 - x1) + (y2 - y1)*(y2 - y1));
		if (x1 == x2 && y1 == y2 && r1 == r2) cout << -1 << '\n';
		else if (r1 + r2 == dis || r1 + dis == r2 || r2 + dis == r1) cout << 1 << '\n';
		else if (dis + r1 < r2 || dis + r2 < r1 || r1+r2 < dis) cout << 0 << '\n';
		else
			cout << 2 << '\n';

	}

	return 0;
}