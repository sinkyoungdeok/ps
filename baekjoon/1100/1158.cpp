#include <cstdio>
#include <algorithm>
#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;
int main()
{
	queue<int> qu;
	vector<int> v;
	int N, M;
	cin >> N >> M;
	for (int i = 1; i <= N; i++)
	{
		v.push_back(i);
	}
	int present = M-1;
	while (N--) {
		qu.push(v[present]);
		v.erase(v.begin() + present, v.begin() + present + 1);
		present += M-1;
		if(N!=0)
			present %= N;
	}
	cout << "<" << qu.front();
	qu.pop();
	while (!qu.empty())
	{
		cout << ", "<<qu.front();
		qu.pop();
	}
	cout << ">" << endl;


	return 0;
}

