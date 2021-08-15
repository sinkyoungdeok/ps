#include <iostream>
#include <queue>
using namespace std;
int main(void)
{
	queue<int> st;
	char num[333335];
	cin >> num;
	for (int i = 0; num[i] != NULL; i++)
	{
		if (num[i] == '0')
		{
			st.push(0);
			st.push(0);
			st.push(0);
		}
		else if (num[i] == '1')
		{
			st.push(0);
			st.push(0);
			st.push(1);
		}
		else if (num[i] == '2')
		{
			st.push(0);
			st.push(1);
			st.push(0);
		}
		else if (num[i] == '3')
		{
			st.push(0);
			st.push(1);
			st.push(1);
		}
		else if (num[i] == '4')
		{
			st.push(1);
			st.push(0);
			st.push(0);
		}
		else if (num[i] == '5')
		{
			st.push(1);
			st.push(0);
			st.push(1);
		}
		else if (num[i] == '6')
		{
			st.push(1);
			st.push(1);
			st.push(0);
		}
		else if (num[i] == '7')
		{
			st.push(1);
			st.push(1);
			st.push(1);
		}
	}
	if (st.front() == 0 && st.size() == 3)
		cout << "0";
	else {

		while (st.front() == 0)
			st.pop();
		while (!st.empty())
		{
			cout << st.front();
			st.pop();
		}
	}
	return 0;
}