#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	char *a = new char[10];
	cin >> a;
	int six = 1;
	int sum = 0;
	for (int i = strlen(a) - 1; i >= 0; i--)
	{
		if (a[i] == 'A')
			sum += 10 * six;
		else if (a[i] == 'B')
			sum += 11 * six;
		else if (a[i] == 'C')
			sum += 12 * six;
		else if (a[i] == 'D')
			sum += 13 * six;
		else if (a[i] == 'E')
			sum += 14 * six;
		else if (a[i] == 'F')
			sum += 15 * six;
		else
			sum += (a[i] - '0') * six;


		six *= 16;
	}
	cout << sum << endl;


	return 0;
}