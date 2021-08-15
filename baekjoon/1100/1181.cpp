#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;
struct A {
	string name;
	int len;
};
class comp {
public:
	bool operator() (A a1, A a2)
	{
		if (a1.len > a2.len)
			return true;
		else if (a1.len == a2.len)
		{
			return a1.name > a2.name;
		}
		else
			return false;
	}
};
int main()
{
	priority_queue<A, vector<A>, comp> pq;
	int n;
	cin >> n;
	while (n--)
	{
		A a;
		cin >> a.name;
		a.len = a.name.length();
		pq.push(a);
	}
	string prevname;
	while (!pq.empty())
	{
		A tmp = pq.top();
		pq.pop();
		if(tmp.name != prevname)
		cout << tmp.name << endl;
		prevname = tmp.name;
	}

	return 0;
}

