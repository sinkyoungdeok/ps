#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	char *a = new char[5];
	int check = 0;
	int num = 0;
	cin >> num;
	for (int i = 1; i <= num; i++)
	{
		int dui = i;
		int j = 0;
		while (dui != 0)
		{
			a[j++] = dui % 10;
			dui /= 10;
		}
		if (j >= 3)
		{
			j--;
			if (a[j] - a[j - 1] == a[j - 1] - a[j - 2])
				check++;
		}
		else
			check++;
	}
	cout << check << endl;

	return 0;
}