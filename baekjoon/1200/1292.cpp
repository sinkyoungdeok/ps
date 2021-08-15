#include <iostream>
using namespace std;
int main()
{
	int *num = new int[10000];
	int numi = 1;
	for (int i = 1; i <= 100; i++)
	{
		for (int j = i; j > 0; j--)
		{
			num[numi++] = i;
		}
	}
	
	int a, b;
	cin >> a >> b;
	int sum = 0;
	for (int i = a; i <= b; i++)
	{
		sum += num[i]; 
	}
	cout << sum << endl;
	return 0;
}