#include <iostream>
using namespace std;
int main()
{
	int num = 0;
	cin >> num;
	if (num < 10)
		num *= 10;
	int nextnum;
	int tens;
	int units;
	int sum;
	int check;
		tens = num / 10;
		units = num % 10;
		sum = tens + units;
		check = 1;
		nextnum = (units * 10) + (sum % 10);
	while (nextnum != num)
	{
		tens = nextnum / 10;
		units = nextnum % 10;
		sum = tens + units;
		check++;
		nextnum = (units * 10) + (sum % 10);
	}
	cout << check << endl;
	return 0;
}