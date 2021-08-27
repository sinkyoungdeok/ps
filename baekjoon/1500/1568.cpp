#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int n = 0;
	cin >> n;
	int sum = 0;
	int song = 1;
	while (n)
	{
		if (n >= song)
		{
			n -= song++;
			sum++;
		}
		else
		{
			song = 1;
		}
	}
	cout << sum << endl;
	return 0;
}