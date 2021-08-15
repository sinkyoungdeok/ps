#include <iostream>
#include <string>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	int m = 0;
	cin >> m;
	if (n % 100 != 0)
	{
		n -= n % 100;
	}
	for (int i = 0; i <= 99; i++)
	{
		if ((n + i) % m == 0)
		{
			if (0 <= i && i <= 9)
				cout << "0" << i << endl;
			else
				cout << i << endl;

			break;
		}
	}

	return 0;
}