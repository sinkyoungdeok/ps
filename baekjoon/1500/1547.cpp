#include <iostream>
using namespace std;
int main()
{
	int n = 0;
	cin >> n;
	int *ball = new int[4];
	ball[1] = 1;
	ball[2] = 0;
	ball[3] = 0;

	for (int i = 0; i < n; i++)
	{
		int num1 = 0;
		int num2 = 0;
		cin >> num1 >> num2;
		int swap = ball[num1];
		ball[num1] = ball[num2];
		ball[num2] = swap;
	}
	for (int i = 1; i <= 3; i++)
	{
		if (ball[i] == 1)
			cout << i << endl;
	}


	return 0;
}