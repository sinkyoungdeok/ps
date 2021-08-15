#include <iostream>
#include <queue>
using namespace std;
class comp {
public:
	bool operator()(const int& a, const int& b) {
		return a>b;
	}

};

priority_queue<int> a;
priority_queue<int,vector<int>, comp> b;
int main()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int a_num = 0;
		cin >> a_num;
		a.push(a_num);
	}
	for (int i = 0; i < n; i++)
	{
		int b_num = 0;
		cin >> b_num;
		b.push(b_num);
	}
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		sum += a.top() * b.top();
		a.pop();
		b.pop();
	}
	cout << sum << endl;

	return 0;
}