#include <iostream>
#include <string>
using namespace std;
int main()
{
	int num[5] = { 0 };
	for (int i = 0; i < 5; i++)
		cin >> num[i];
	
	for (int i = 1;; i++)
	{
		int cnt = 0;
		for (int j = 0; j < 5; j++)
			if (i % num[j] == 0)
				cnt++;
		if (cnt >= 3)
		{
			cout << i << endl;
			return 0;
		}

	}



	return 0;
}