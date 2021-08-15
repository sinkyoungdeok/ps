#include <iostream>
using namespace std;
int main()
{
	int *a = new int[5000];
	int sum = 0;
	long long int num = 0;
	int dui = 0;
	int startnum = 0;
	cin >> num;
	if (num == 1)
		cout << "1/1" << endl;
	else {
		for (int i = 1; i <= 5000; i++)
		{
			sum = sum + i;
			a[i] = sum;
			if (sum >= num)
			{
				dui = i;
				break;
			}
		}
		startnum = a[dui] - a[dui - 1];
		int j = 1;
		int count = 1;
		int k = startnum;
		while (1)
		{
			if (num == a[dui - 1] + count)
				break;
			else
			{
				j++; k--;
				count++;
			}

		}

		if (startnum % 2 == 0)
			cout << j << "/" << k << endl;
		else
			cout << k << "/" << j << endl;
	}
	return 0;
}