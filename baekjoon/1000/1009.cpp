#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int a, b;
		cin >> a >> b;
		int sum = 1;
		while (b--)
		{
			sum *= a;
			sum %= 10;
		}
		if (sum == 0)
			cout << "10" << endl;
		else
		cout << sum << endl;
	}
	return 0;
}