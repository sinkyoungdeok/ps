#include <iostream>
using namespace std;
int main()
{
	char *num = new char[10];
	cin >> num;
	int *num_check = new int[10];
	int check = 0;
	for (int i = 0; i<10; i++)
		num_check[i] = 0;
	for (int i = 0; num[i] != 0; i++)
	{
		if (num[i] == '6' || num[i] == '9')
		{
			if (num_check[6] >= num_check[9])
				num_check[9]++;
			else
				num_check[6]++;
		}
		else
			num_check[num[i]-'0'] ++;
	}
	int maxcheck = 0;
	for (int i = 0; i < 10; i++)
		if (maxcheck < num_check[i])
			maxcheck = num_check[i];

	cout << maxcheck << endl;

	return 0;
}