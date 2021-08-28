#include <iostream>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	int check = 0;
	for (int i = 1; i <= n; i++)
	{
		if (i % 5 == 0)
		{
			check++;
			if (i % 25 == 0)
			{
				check++;
				if (i % 125 == 0)
					check++;
			}
			
		}
	}
	cout << check << endl;


	return 0;
}