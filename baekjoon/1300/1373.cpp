#include <iostream>
#include <stack>
#include <cstring>
using namespace std;
int main(void)
{
	stack<int> st;
	char num[1000001];
	cin >> num;
	int mid_sum = 0;
	int two = 1;
	for (int i = strlen(num) - 1; i >= 0; i--)
	{
		mid_sum += two * (num[i] -'0');
		two *= 2;
		if (two == 8)
		{
			two = 1;
			st.push(mid_sum);
			mid_sum = 0;
		}
	}
	st.push(mid_sum);

	if (st.top() == 0 && st.size() ==1)
	{
		cout << "0";
	}
	else {
		while (st.top() == 0)
			st.pop();
		while (!st.empty())
		{
			cout << st.top();
			st.pop();
		}
	}

	return 0;
}