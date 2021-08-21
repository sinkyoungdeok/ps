#include <iostream>
#include <stack>
#include <cstring>
using namespace std;
int main(void)
{
	int n = 0;
	cin >> n;
	char num[20];
	int numi = 0;
	while (n)
	{
		num[numi++] = n % 10;
		n /= 10;
	}
	int check = 0;
	for (int i = 0; i < numi-1; i++)
	{
		unsigned long long int sum1= 1;
		unsigned long long int sum2 = 1;
		for (int j = 0; j <= i; j++)
		{
			sum1 *= num[j];
		}
		for (int j = i + 1; j < numi; j++)
		{
			sum2 *= num[j];
		}
		if (sum1 == sum2)
			check = 1;
	}
	if (check == 0)
		cout << "NO" << endl;
	else
		cout << "YES" << endl;


	return 0;
}