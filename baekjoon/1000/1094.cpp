#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int num = 0;
	int check = 0;
	int initial = 64;
	cin >> num;
	int sum = 0;
	while(1)
	{
		while (( sum+ initial) > num)
		{
			initial = initial / 2;
		}
		sum = sum + initial;
		check++;
		//cout << "sum:" << sum << "check:" << check << endl;
		if (sum == num)
			break;

	}
	cout << check << endl;


	return 0;
}