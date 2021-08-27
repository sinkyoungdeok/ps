#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	for (int i = n; i > 0; i--)
	{
		int j = i;
		int check = 0;
		while (j != 0)
		{
			if (j % 10 != 7 && j % 10 != 4)
			{
				check = 1;
				break;
			}
			j /= 10;
		}
		if (check == 1)
			continue;
		else
		{
			cout << i << endl;
			break;
		}
	

	}
	return 0;
}