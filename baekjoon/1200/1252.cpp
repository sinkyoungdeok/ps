#include <iostream>
#include <stack>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
	stack<int> st;
	char num1[81];
	char num2[81];
	cin >> num1 >> num2;
		int n1_len = strlen(num1) - 1;
		int n2_len = strlen(num2) - 1;
		int carry = 0;
		while (n1_len > -1 && n2_len > -1) {
			int num = num1[n1_len--] - '0' + num2[n2_len--] - '0' + carry;
			if (num == 0 || num == 1)
				carry = 0;
			else
			{
				carry = 1;
				num %= 2;
			}
			st.push(num);
		}
		while (n1_len > -1)
		{
			int num = num1[n1_len--] - '0' + carry;
			if (num == 0 || num == 1)
				carry = 0;
			else
			{
				carry = 1;
				num %= 2;
			}
			st.push(num);
		}

		while (n2_len > -1)
		{
			int num = num2[n2_len--] - '0' + carry;
			if (num == 0 || num == 1)
				carry = 0;
			else
			{
				carry = 1;
				num %= 2;
			}
			st.push(num);
		}
		if (carry == 1)
			st.push(carry);

		while (st.top() == 0)
		{
			st.pop();
			if (st.empty() == 1)
				break;
		}
		if (st.empty() == 1) {
			cout << "0" << endl;
			return 0;
		}

		while (!st.empty()) {
			cout << st.top();
			st.pop();
		}
		cout << endl;
	return 0;
}