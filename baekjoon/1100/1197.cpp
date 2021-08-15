#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
using namespace std;
struct abc {
	short a, b;
	int c;
};
class comp {
public:
	bool operator() (abc abc1, abc abc2)
	{
		return abc1.c > abc2.c;
	}
};
short Find_Set(short *parent, short x);
int main(int argc, char **argv)
{
	//ios_base::sync_with_stdio(false);
	//cin.tie(NULL);
	//cout.tie(NULL);
	long long int result = 0;
	short n;
	int m;
	cin >> n >> m;
	short *parent = new short[n + 1];
	for (short i = 1; i <= n; i++)
		parent[i] = i;
	priority_queue<abc,vector<abc>,comp> pq;
	for (int i = 0; i < m; i++)
	{
		abc tmp;
		cin >> tmp.a >> tmp.b >> tmp.c;
		pq.push(tmp);
	}
	while (!pq.empty())
	{
		abc tmp = pq.top(); pq.pop();
		if (Find_Set(parent, tmp.a) != Find_Set(parent, tmp.b))
		{
			result += tmp.c;
			parent[Find_Set(parent, tmp.a)] = Find_Set(parent, tmp.b);

		}
	}
	cout << result << endl;
	return 0;
}

short Find_Set(short *parent, short x)
{
	if (x == parent[x]) return x;
	else return parent[x] = Find_Set(parent, parent[x]);
}